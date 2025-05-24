"""empty message

Revision ID: f007cd3428fd
Revises: 4ca9025dd74c
Create Date: 2025-05-24 12:21:43.002924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision: str = 'f007cd3428fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('phone', sa.String(length=50)),
        sa.Column('email', sa.String(length=100))
    )

    # Создание таблицы voyages
    op.create_table(
        'parts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('type', sa.String(length=100), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('capacity', sa.Integer(), nullable=False),
    )
    

    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('customer_id', sa.Integer(), ForeignKey('customers.id'), nullable=False),
        sa.Column('description', sa.String(length=255)),
        sa.Column('fix_part_id', sa.Integer(), ForeignKey('parts.id'))
    )



def downgrade() -> None:
    """Downgrade schema."""
    pass
