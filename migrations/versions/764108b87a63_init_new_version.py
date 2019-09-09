"""init new version 

Revision ID: 764108b87a63
Revises: 
Create Date: 2019-09-09 11:04:55.179000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '764108b87a63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bar_user')
    op.drop_table('location')
    op.drop_table('move_base_goal')
    op.drop_table('bar_ber')
    op.drop_table('hibernate_sequence')
    op.drop_table('barber_order')
    op.drop_table('barber_robbing_order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('barber_robbing_order',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('hair_desc', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('hairdresser_get', mysql.BIT(length=1), nullable=False),
    sa.Column('hairdresser_tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('latitude', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('order_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('user_get', mysql.BIT(length=1), nullable=False),
    sa.Column('user_tel', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'MyISAM'
    )
    op.create_table('barber_order',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('comment', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('commented', mysql.BIT(length=1), nullable=False),
    sa.Column('cut', mysql.BIT(length=1), nullable=False),
    sa.Column('date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('hair_desc', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('hair_img_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('hairdresser_comment', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('hairdresser_tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('user_tel', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'MyISAM'
    )
    op.create_table('hibernate_sequence',
    sa.Column('next_val', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'MyISAM'
    )
    op.create_table('bar_ber',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('business_license', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('auth', mysql.BIT(length=1), nullable=False),
    sa.Column('img_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('location', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('store_name', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'MyISAM'
    )
    op.create_table('move_base_goal',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False, comment=u'id'),
    sa.Column('position_x', mysql.FLOAT(), nullable=False),
    sa.Column('position_y', mysql.FLOAT(), nullable=False),
    sa.Column('position_z', mysql.FLOAT(), nullable=False),
    sa.Column('orientation_x', mysql.FLOAT(), nullable=False),
    sa.Column('orientation_y', mysql.FLOAT(), nullable=False),
    sa.Column('orientation_z', mysql.FLOAT(), nullable=False),
    sa.Column('orientation_w', mysql.FLOAT(), nullable=False),
    sa.Column('location', mysql.TEXT(), nullable=False, comment=u'?????????'),
    sa.PrimaryKeyConstraint('id'),
    comment=u'?????????',
    mysql_comment=u'?????????',
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'InnoDB'
    )
    op.create_table('location',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('location', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'InnoDB'
    )
    op.create_table('bar_user',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('business_license', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('idcard_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('barber_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('img_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('preparing', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('role', mysql.BIT(length=1), nullable=False),
    sa.Column('salt', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('user_name', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'MyISAM'
    )
    # ### end Alembic commands ###
