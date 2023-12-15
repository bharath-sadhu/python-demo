"""update_planet

Revision ID: 3bc9540bdccd
Revises: 490952384afc
Create Date: 2023-12-15 15:46:38.429015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3bc9540bdccd"
down_revision: Union[str, None] = "490952384afc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "planets", sa.Column("system_id", sa.UUID(), nullable=False), schema="interview"
    )
    op.create_foreign_key(
        op.f("planets_system_id_fkey"),
        "planets",
        "systems",
        ["system_id"],
        ["id"],
        source_schema="interview",
        referent_schema="interview",
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("planets_system_id_fkey"),
        "planets",
        schema="interview",
        type_="foreignkey",
    )
    op.drop_column("planets", "system_id", schema="interview")
    # ### end Alembic commands ###
