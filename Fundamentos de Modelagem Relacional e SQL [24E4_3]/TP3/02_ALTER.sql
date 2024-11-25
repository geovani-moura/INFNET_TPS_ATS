--C
ALTER TABLE Clientes
MODIFY COLUMN Preferencias VARCHAR(500);

--D
ALTER TABLE Fornecedores
CHANGE COLUMN NomeFornecedor Nome VARCHAR(100);

ALTER TABLE Produtos
CHANGE COLUMN Descricao DescricaoProduto TEXT;

--E
ALTER TABLE Produtos
MODIFY COLUMN Preco DECIMAL(12, 2);

--F
UPDATE Clientes
SET Endereco = 'Nova Rua A, 123'
WHERE ClienteID = 1;

UPDATE Produtos
SET Preco = 180.00
WHERE ProdutoID = 3;

UPDATE Vendas
SET StatusVenda = 'Concluída'
WHERE VendaID = 1;

--G
DELETE FROM Clientes WHERE ClienteID = 5;
DELETE FROM Produtos WHERE ProdutoID = 4;
DELETE FROM Vendas WHERE VendaID = 2;

--H
DROP TABLE LogVendas;












ALTER TABLE Clientes DROP COLUMN Preferencias;

ALTER TABLE Clientes CHANGE COLUMN Telefone ContatoTelefone VARCHAR(20);
ALTER TABLE Fornecedores CHANGE COLUMN Contato TelefoneContato VARCHAR(50);

ALTER TABLE Produtos MODIFY COLUMN Preco DECIMAL(12, 2);

UPDATE Clientes SET ContatoTelefone = '31988888888' WHERE ClienteID = 3;
UPDATE Produtos SET Descricao = 'Espumante Brut Premium - Edição Especial' WHERE ProdutoID = 2;
UPDATE Vendas SET StatusVenda = 'Concluída' WHERE VendaID = 3;


