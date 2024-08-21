from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    phone: str
    meus_produtos: List[Produtos]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]

class Produto(BaselModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    disponivel: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
