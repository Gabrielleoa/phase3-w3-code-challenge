"""favorite restaurant

Revision ID: 736837ac697c
Revises: 1083d035b224
Create Date: 2024-01-08 01:56:41.837922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '736837ac697c'
down_revision: Union[str, None] = '1083d035b224'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
