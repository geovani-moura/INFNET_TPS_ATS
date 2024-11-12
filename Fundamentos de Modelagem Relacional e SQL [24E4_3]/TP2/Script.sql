CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Telefone VARCHAR(20),
    Endereco VARCHAR(255),
    Preferencias TEXT
);

CREATE TABLE Fornecedores (
    FornecedorID INT PRIMARY KEY,
    NomeFornecedor VARCHAR(100) NOT NULL,
    Contato VARCHAR(50),
    Endereco VARCHAR(255)
);

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50),
    Descricao TEXT,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT DEFAULT 0,
    FornecedorID INT,
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

CREATE TABLE Vendas (
    VendaID INT PRIMARY KEY,
    ClienteID INT NOT NULL,
    DataVenda DATETIME DEFAULT CURRENT_TIMESTAMP,
    ValorTotal DECIMAL(10, 2),
    StatusVenda VARCHAR(20),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

CREATE TABLE ItensVenda (
    ItemID INT PRIMARY KEY,
    VendaID INT NOT NULL,
    ProdutoID INT NOT NULL,
    Quantidade INT NOT NULL,
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

CREATE TABLE Pagamentos (
    PagamentoID INT PRIMARY KEY,
    VendaID INT NOT NULL,
    ValorPago DECIMAL(10, 2),
    DataPagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    MetodoPagamento VARCHAR(50),
    StatusPagamento VARCHAR(20),
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID)
);

--Tabela implementada para o Item 4.0.
CREATE TABLE Venda_Produto (
    VendaID INT,
    ProdutoID INT,
    Quantidade INT NOT NULL,  
    PRIMARY KEY (VendaID, ProdutoID), 
    FOREIGN KEY (VendaID) REFERENCES Vendas(VendaID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

--Itens criados para o item 5.0
CREATE OR ALTER PROCEDURE RealizarVenda(
    IN p_ClienteID INT,
    IN p_ProdutoID INT,
    IN p_Quantidade INT
)
BEGIN
    DECLARE estoque_atual INT;
    DECLARE v_VendaID INT;
    
    SELECT Estoque INTO estoque_atual
    FROM Produtos
    WHERE ProdutoID = p_ProdutoID;
    
    IF estoque_atual < p_Quantidade THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Estoque insuficiente para a venda.';
    ELSE
        INSERT INTO Vendas (ClienteID, ValorTotal, StatusVenda)
        VALUES (p_ClienteID, 0, 'Em andamento');
        
        SET v_VendaID = LAST_INSERT_ID();
        
        INSERT INTO ItensVenda (VendaID, ProdutoID, Quantidade)
        VALUES (v_VendaID, p_ProdutoID, p_Quantidade);
        
        UPDATE Produtos
        SET Estoque = Estoque - p_Quantidade
        WHERE ProdutoID = p_ProdutoID;
    END IF;
END

--CALL RealizarVenda(1, 101, 3);  -- Cliente 1 comprando 3 unidades do produto 101
