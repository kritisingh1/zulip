# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from zerver.lib.migrate import create_index_if_not_exist  # nolint


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0098_index_has_alert_word_user_messages'),
    ]

    operations = [
        migrations.RunSQL(
            create_index_if_not_exist(
                index_name='zerver_usermessage_wildcard_mentioned_message_id',
                table_name='zerver_usermessage',
                column_string='user_profile_id, message_id',
                where_clause='WHERE (flags & 8) != 0 OR (flags & 16) != 0',
            ),
            reverse_sql='DROP INDEX zerver_usermessage_wilcard_mentioned_message_id;'
        ),
    ]
