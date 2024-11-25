CREATE TABLE IF NOT EXISTS Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Telefone VARCHAR(20),
    Endereco VARCHAR(255),
    Preferencias TEXT
);

CREATE TABLE IF NOT EXISTS Fornecedores (
    FornecedorID INT PRIMARY KEY,
    NomeFornecedor VARCHAR(100) NOT NULL,
    Contato VARCHAR(50),
    Endereco VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50),
    Descricao TEXT,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT DEFAULT 0,
    FornecedorID INT,
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

CREATE TABLE IF NOT EXISTS Vendas (
    VendaID INT PRIMARY KEY,
    ClienteID INT NOT NULL,
    DataVenda DATETIME DEFAULT CURRENT_TIMESTAMP,
    ValorTotal DECIMAL(10, 2),
    StatusVenda VARCHAR(20),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

CREATE TABLE IF NOT EXISTS ItensVenda (
    ItemID INT PRIMARY KEY,
    VendaID INT NOT NULL,
    ProdutoID INT NOT NULL,
    Quantidade INT NOT NULL,
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

CREATE TABLE IF NOT EXISTS Pagamentos (
    PagamentoID INT PRIMARY KEY,
    VendaID INT NOT NULL,
    ValorPago DECIMAL(10, 2),
    DataPagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    MetodoPagamento VARCHAR(50),
    StatusPagamento VARCHAR(20),
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID)
);

--Tabela implementada para o Item 4.0.
CREATE TABLE IF NOT EXISTS Venda_Produto (
    VendaID INT,
    ProdutoID INT,
    Quantidade INT NOT NULL,  
    PRIMARY KEY (VendaID, ProdutoID), 
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

--Tabela implementada para o TP3
CREATE TABLE IF NOT EXISTS Promocoes (
    PromocaoID INT PRIMARY KEY,
    NomePromocao VARCHAR(100) NOT NULL,
    PercentualDesconto DECIMAL(5, 2) NOT NULL,
    DataInicio DATE NOT NULL,
    DataFim DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Produto_Promocao (
    ProdutoID INT,
    PromocaoID INT,
    PRIMARY KEY (ProdutoID, PromocaoID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (PromocaoID) REFERENCES Promocoes(PromocaoID)
);

CREATE TABLE IF NOT EXISTS LogVendas (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    VendaID INT NOT NULL,
    DataHora DATETIME DEFAULT CURRENT_TIMESTAMP,
    Descricao TEXT
);

--Itens alterado para levar em conta a promoção
CREATE OR ALTER PROCEDURE RealizarVenda(
    IN p_ClienteID INT,
    IN p_ProdutoID INT,
    IN p_Quantidade INT
)
BEGIN
    DECLARE estoque_atual INT;
    DECLARE v_VendaID INT;
    DECLARE preco_unitario DECIMAL(10, 2);
    DECLARE desconto_promocao DECIMAL(5, 2);
    DECLARE valor_total DECIMAL(10, 2);

    SELECT Estoque INTO estoque_atual
    FROM Produtos
    WHERE ProdutoID = p_ProdutoID;

    IF estoque_atual < p_Quantidade THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estoque insuficiente para a venda.';
    ELSE
        SELECT 
            Preco,
            COALESCE(MAX(P.Desconto), 0) INTO preco_unitario, desconto_promocao
        FROM Produtos Pr
        LEFT JOIN Produto_Promocao PP ON Pr.ProdutoID = PP.ProdutoID
        LEFT JOIN Promocoes P 
            ON PP.PromocaoID = P.PromocaoID
            AND CURDATE() BETWEEN P.DataInicio AND P.DataFim
        WHERE Pr.ProdutoID = p_ProdutoID;

        SET valor_total = p_Quantidade * preco_unitario * (1 - (desconto_promocao / 100));

        INSERT INTO Vendas (ClienteID, ValorTotal, StatusVenda)
        VALUES (p_ClienteID, valor_total, 'Em andamento');

        SET v_VendaID = LAST_INSERT_ID();

        INSERT INTO ItensVenda (VendaID, ProdutoID, Quantidade)
        VALUES (v_VendaID, p_ProdutoID, p_Quantidade);

        UPDATE Produtos
        SET Estoque = Estoque - p_Quantidade
        WHERE ProdutoID = p_ProdutoID;

        IF EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'LogVendas') THEN
            INSERT INTO LogVendas (VendaID, Descricao)
            VALUES (v_VendaID, CONCAT('Venda realizada para ClienteID: ', p_ClienteID, ', ProdutoID: ', p_ProdutoID, ', Quantidade: ', p_Quantidade));
        END IF;
    END IF;
END;

--CALL RealizarVenda(1, 101, 3);  -- Cliente 1 comprando 3 unidades do produto 101


















