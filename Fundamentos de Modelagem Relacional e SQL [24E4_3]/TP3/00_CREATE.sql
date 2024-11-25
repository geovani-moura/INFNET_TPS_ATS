-- drop table if exists ItensVenda 
-- drop table if exists LogVendas
-- drop table if exists Produto_Promocao
-- drop table if exists Venda_Produto
-- drop table if exists Pagamentos
-- drop table if exists Vendas
-- drop table if exists Produtos
-- drop table if exists Promocoes
-- drop table if exists Fornecedores
-- drop table if exists Clientes

create table Clientes (
    ClienteID int primary key,
    Nome varchar(100) not null,
    Email varchar(100) unique,
    Telefone varchar(20),
    Endereco varchar(255),
    Preferencias text
);

create table Fornecedores (
    FornecedorID int primary key,
    NomeFornecedor varchar(100) not null,
    Contato varchar(50),
    Endereco varchar(255)
);

create table Produtos (
    ProdutoID int primary key,
    NomeProduto varchar(100) not null,
    Categoria varchar(50),
    Descricao text,
    Preco decimal(10, 2) not null,
    Estoque int default 0,
    FornecedorID int,
    foreign key (FornecedorID) references Fornecedores(FornecedorID)
);

create table Vendas (
    VendaID int primary key,
    ClienteID int not null,
    DataVenda datetime default current_timestamp,
    ValorTotal decimal(10, 2),
    StatusVenda varchar(20),
    foreign key (ClienteID) references Clientes(ClienteID)
);

create table ItensVenda (
    ItemID int primary key,
    VendaID int not null,
    ProdutoID int not null,
    Quantidade int not null,
    foreign key (VendaID) references Vendas(VendaID),
    foreign key (ProdutoID) references Produtos(ProdutoID)
);

create table Pagamentos (
    PagamentoID int primary key,
    VendaID int not null,
    ValorPago decimal(10, 2),
    DataPagamento datetime default current_timestamp,
    MetodoPagamento varchar(50),
    StatusPagamento varchar(20),
    foreign key (VendaID) references Vendas(VendaID)
);

create table Venda_Produto (
    VendaID int,
    ProdutoID int,
    Quantidade int not null,  
    primary key (VendaID, ProdutoID), 
    foreign key (VendaID) references Vendas(VendaID),
    foreign key (ProdutoID) references Produtos(ProdutoID)
);

create table Promocoes (
    PromocaoID int primary key,
    NomePromocao varchar(100) not null,
    PercentualDesconto decimal(5, 2) not null,
    DataInicio date not null,
    DataFim date not null
);

create table Produto_Promocao (
    ProdutoID int,
    PromocaoID int,
    primary key (ProdutoID, PromocaoID),
    foreign key (ProdutoID) references Produtos(ProdutoID),
    foreign key (PromocaoID) references Promocoes(PromocaoID)
);

create table LogVendas (
    LogID int primary key auto_increment,
    VendaID int not null,
    DataHora datetime default current_timestamp,
    Descricao text
);

create procedure RealizarVenda(
    in p_ClienteID int,
    in p_ProdutoID int,
    in p_Quantidade int
)
begin
    declare estoque_atual int;
    declare v_VendaID int;
    declare preco_unitario decimal(10, 2);
    declare desconto_promocao decimal(5, 2);
    declare valor_total decimal(10, 2);

    select Estoque into estoque_atual
    from Produtos
    where ProdutoID = p_ProdutoID;

    if estoque_atual < p_Quantidade then
        signal sqlstate '45000'
        set message_text = 'Estoque insuficiente para a venda.';
    else
        select 
            Preco,
            coalesce(max(P.Desconto), 0) into preco_unitario, desconto_promocao
        from Produtos Pr
        left join Produto_Promocao PP on Pr.ProdutoID = PP.ProdutoID
        left join Promocoes P 
            on PP.PromocaoID = P.PromocaoID
            and curdate() between P.DataInicio and P.DataFim
        where Pr.ProdutoID = p_ProdutoID;

        set valor_total = p_Quantidade * preco_unitario * (1 - (desconto_promocao / 100));

        insert into Vendas (ClienteID, ValorTotal, StatusVenda)
        values (p_ClienteID, valor_total, 'Em andamento');

        set v_VendaID = last_insert_id();

        insert into ItensVenda (VendaID, ProdutoID, Quantidade)
        values (v_VendaID, p_ProdutoID, p_Quantidade);

        update Produtos
        set Estoque = Estoque - p_Quantidade
        where ProdutoID = p_ProdutoID;

        if exists (select 1 from information_schema.tables where table_name = 'LogVendas') then
            insert into LogVendas (VendaID, Descricao)
            values (v_VendaID, concat('Venda realizada para ClienteID: ', p_ClienteID, ', ProdutoID: ', p_ProdutoID, ', Quantidade: ', p_Quantidade));
        end if;
    end if;
end;

--call RealizarVenda(1, 101, 3);  -- Cliente 1 comprando 3 unidades do produto 101
