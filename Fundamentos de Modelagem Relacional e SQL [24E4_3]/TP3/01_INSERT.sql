INSERT INTO Clientes (ClienteID, Nome, Email, Telefone, Endereco, Preferencias) VALUES
(1, 'Carlos Silva', 'carlos.silva@example.com', '11987654321', 'Rua A, 123', 'Vinhos tintos'),
(2, 'Ana Costa', 'ana.costa@example.com', '21987654321', 'Rua B, 456', 'Espumantes'),
(3, 'João Souza', 'joao.souza@example.com', '31987654321', 'Rua C, 789', 'Vinhos brancos'),
(4, 'Mariana Oliveira', 'mariana.oliveira@example.com', '41987654321', 'Rua D, 101', 'Vinhos rosé'),
(5, 'Pedro Santos', 'pedro.santos@example.com', '51987654321', 'Rua E, 202', 'Destilados');

INSERT INTO Fornecedores (FornecedorID, NomeFornecedor, Contato, Endereco) VALUES
(1, 'Adega Brasil', 'contato@adegabrasil.com', 'Av. Central, 1000'),
(2, 'Vinhos Importados', 'vendas@vinhosimportados.com', 'Av. Europa, 500'),
(3, 'Bebidas Fina', 'suporte@bebidasfina.com', 'Rua das Flores, 200'),
(4, 'Espumantes Luxo', 'luxo@espumantesluxo.com', 'Rua do Champanhe, 300'),
(5, 'Cachaçaria Premium', 'contato@cachacaria.com', 'Av. Colonial, 400');

INSERT INTO Produtos (ProdutoID, NomeProduto, Categoria, Descricao, Preco, Estoque, FornecedorID) VALUES
(101, 'Vinho Tinto Reserva', 'Vinho Tinto', 'Vinho tinto de alta qualidade', 120.00, 50, 1),
(102, 'Espumante Brut', 'Espumante', 'Espumante seco e elegante', 80.00, 30, 4),
(103, 'Vinho Branco Chardonnay', 'Vinho Branco', 'Vinho branco aromático', 95.00, 40, 2),
(104, 'Cachaça Artesanal', 'Destilado', 'Cachaça premium artesanal', 45.00, 100, 5),
(105, 'Rosé Provence', 'Vinho Rosé', 'Vinho rosé refrescante', 110.00, 25, 3);

INSERT INTO Vendas (VendaID, ClienteID, DataVenda, ValorTotal, StatusVenda) VALUES
(1, 1, '2024-11-25 10:00:00', 240.00, 'Concluída'),
(2, 2, '2024-11-25 11:00:00', 160.00, 'Concluída'),
(3, 3, '2024-11-25 12:00:00', 285.00, 'Concluída'),
(4, 4, '2024-11-25 13:00:00', 450.00, 'Concluída'),
(5, 5, '2024-11-25 14:00:00', 90.00, 'Concluída');

INSERT INTO ItensVenda (ItemID, VendaID, ProdutoID, Quantidade) VALUES
(1, 1, 101, 2),
(2, 2, 102, 2),
(3, 3, 103, 3),	
(4, 4, 105, 4),
(5, 5, 104, 2);

INSERT INTO Pagamentos (PagamentoID, VendaID, ValorPago, DataPagamento, MetodoPagamento, StatusPagamento) VALUES
(1, 1, 240.00, '2024-11-25 10:30:00', 'Cartão de Crédito', 'Aprovado'),
(2, 2, 160.00, '2024-11-25 11:30:00', 'Pix', 'Aprovado'),
(3, 3, 285.00, '2024-11-25 12:30:00', 'Boleto', 'Aprovado'),
(4, 4, 450.00, '2024-11-25 13:30:00', 'Dinheiro', 'Aprovado'),
(5, 5, 90.00, '2024-11-25 14:30:00', 'Cartão de Débito', 'Aprovado');

INSERT INTO Promocoes (PromocaoID, NomePromocao, Desconto, DataInicio, DataFim) VALUES
(1, 'Black Friday', 20.00, '2024-11-20', '2024-11-30'),
(2, 'Natal Premiado', 15.00, '2024-12-01', '2024-12-25'),
(3, 'Ano Novo', 10.00, '2025-01-01', '2025-01-10'),
(4, 'Promoção Verão', 25.00, '2025-01-15', '2025-02-15'),
(5, 'Queima de Estoque', 30.00, '2025-03-01', '2025-03-31');

INSERT INTO Produto_Promocao (ProdutoID, PromocaoID) VALUES
(101, 1),
(102, 2),
(103, 3),
(104, 4),
(105, 5);
