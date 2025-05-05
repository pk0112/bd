"""empty message

Revision ID: 4ca9025dd74c
Revises: 
Create Date: 2025-05-05 14:07:24.015368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision: str = '4ca9025dd74c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Создание таблицы vessels
    op.create_table(
        'vessels',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('type', sa.String(length=50)),
        sa.Column('capacity', sa.DECIMAL(10, 2))
    )

    # Создание таблицы ports
    op.create_table(
        'ports',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('location', sa.String(length=255))
    )

    # Создание таблицы voyages
    op.create_table(
        'voyages',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('vessel_id', sa.Integer(), ForeignKey('vessels.id'), nullable=False),
        sa.Column('start_port_id', sa.Integer(), ForeignKey('ports.id'), nullable=False),
        sa.Column('end_port_id', sa.Integer(), ForeignKey('ports.id'), nullable=False),
        sa.Column('departure_DateTime', sa.DateTime()),
        sa.Column('arrival_DateTime', sa.DateTime())
    )

    # Создание таблицы shipments
    op.create_table(
        'shipments',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('voyage_id', sa.Integer(), ForeignKey('voyages.id'), nullable=False),
        sa.Column('cargo_description', sa.String(length=255)),
        sa.Column('weight', sa.DECIMAL(10, 2)),
        sa.Column('shipped_date', sa.DateTime())
    )

    # Создание таблицы personnel
    op.create_table(
        'personnel',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('role', sa.String(length=50))
    )

    # Создание таблицы port_calls
    op.create_table(
        'port_calls',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('voyage_id', sa.Integer(), ForeignKey('voyages.id')),
        sa.Column('port_id', sa.Integer(), ForeignKey('ports.id')),
        sa.Column('arrival_time', sa.DateTime()),
        sa.Column('departure_time', sa.DateTime()),
        # Добавление колонки responsible_personnel_id
        sa.Column('responsible_personnel_id',sa.Integer(),ForeignKey("personnel.id")),
    )


def downgrade():
    op.drop_table('port_calls')
    op.drop_table ('shipments')
    op.drop_table ('voyages')
    op.drop_table ('ports')
    op.drop_table ('vessels')
    op.drop_table ('personnel')