"""relationship init"


Revision ID: 1083d035b224
Revises: 9433efd7289f
Create Date: 2024-01-08 01:53:34.724429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1083d035b224'
down_revision: Union[str, None] = '9433efd7289f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
