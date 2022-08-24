"""empty message

Revision ID: 835c578ad90b
Revises: 6902e1ae25ae
Create Date: 2022-08-24 00:11:07.702441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '835c578ad90b'
down_revision = '6902e1ae25ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###