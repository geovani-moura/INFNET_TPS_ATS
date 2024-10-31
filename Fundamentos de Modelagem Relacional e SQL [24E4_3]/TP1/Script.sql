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

