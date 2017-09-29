"""Adds external ID checking and modifying enum

Revision ID: b29e2c4bf8c9
Revises: 1ae8e3104db8
Create Date: 2017-09-26 10:50:35.740367

"""

# revision identifiers, used by Alembic.
revision = 'b29e2c4bf8c9'
down_revision = '1ae8e3104db8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificates', sa.Column('external_id', sa.String(128), nullable=True))
    op.sync_enum_values('public', 'log_type', ['create_cert', 'key_view', 'update_cert'], ['create_cert', 'key_view', 'revoke_cert', 'update_cert'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values('public', 'log_type', ['create_cert', 'key_view', 'revoke_cert', 'update_cert'], ['create_cert', 'key_view', 'update_cert'])
    op.drop_column('certificates', 'external_id')
    # ### end Alembic commands ###
