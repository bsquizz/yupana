#
# Copyright 2019 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Test the LegacyReport API."""

import uuid
from datetime import datetime

from django.test import TestCase

from api.legacy_report.model import LegacyReport


class LegacyReportModelTest(TestCase):
    """Tests against the LegacyReport model."""

    def setUp(self):
        """Create test case setup."""
        self.uuid = str(uuid.uuid4())
        self.upload_srv_msg = {'accountid': '13423',
                               'msg_url': 'foo'}
        self.date = datetime.now()
        self.report = LegacyReport(
            report_platform_id=self.uuid,
            upload_srv_kafka_msg=self.upload_srv_msg,
            account='13423',
            request_id='12345',
            state=LegacyReport.NEW,
            state_info=[LegacyReport.NEW],
            retry_count=0,
            last_update_time=self.date,
            ready_to_archive=False,
            arrival_time=self.date,
            processing_start_time=self.date)

    def test_report_fields(self):
        """Test the report fields."""
        self.assertEqual(self.report.report_platform_id, self.uuid)
        self.assertEqual(self.report.upload_srv_kafka_msg,
                         self.upload_srv_msg)
        self.assertEqual(self.report.ready_to_archive, False)
        self.assertEqual(self.report.state, LegacyReport.NEW)
        self.assertEqual(self.report.state_info, [LegacyReport.NEW])
        self.assertEqual(self.report.last_update_time, self.date)
        # pylint: disable=line-too-long
        expected = "{report_platform_id:%s, host_inventory_api_version: None, source: None, source_metadata: None, account: 13423, request_id: 12345, upload_ack_status: None, upload_srv_kafka_msg: {'accountid': '13423', 'msg_url': 'foo'}, git_commit: None, state: new, state_info: ['new'], retry_count: 0, retry_type: time, last_update_time: %s, arrival_time: %s, processing_start_time: %s, processing_end_time: None }" % (self.uuid, self.date, self.date, self.date)  # noqa
        self.assertEqual(str(self.report), expected)