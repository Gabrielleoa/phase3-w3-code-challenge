"""final revision

Revision ID: ac4b8ebd5d24
Revises: 736837ac697c
Create Date: 2024-01-08 01:59:17.064404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac4b8ebd5d24'
down_revision: Union[str, None] = '736837ac697c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
