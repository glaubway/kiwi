from nose.tools import *
from mock import patch

import mock

import nose_helper

from kiwi.exceptions import *
from kiwi.disk_format import DiskFormat


class TestDiskFormat(object):
    @raises(KiwiDiskFormatSetupError)
    def test_format_not_implemented(self):
        DiskFormat('foo', mock.Mock(), 'source_dir', 'target_dir')

    @patch('kiwi.disk_format.DiskFormatQcow2')
    def test_disk_format_qcow2(self, mock_qcow2):
        xml_state = mock.Mock()
        DiskFormat('qcow2', xml_state, 'source_dir', 'target_dir')
        mock_qcow2.assert_called_once_with(
            xml_state, 'source_dir', 'target_dir', None
        )

    @patch('kiwi.disk_format.DiskFormatVhd')
    def test_disk_format_vhd(self, mock_vhd):
        xml_state = mock.Mock()
        DiskFormat('vhd', xml_state, 'source_dir', 'target_dir')
        mock_vhd.assert_called_once_with(
            xml_state, 'source_dir', 'target_dir', None
        )

    @patch('kiwi.disk_format.DiskFormatVhdFixed')
    def test_disk_format_vhdfixed(self, mock_vhdfixed):
        xml_state = mock.Mock()
        DiskFormat('vhdfixed', xml_state, 'source_dir', 'target_dir')
        mock_vhdfixed.assert_called_once_with(
            xml_state, 'source_dir', 'target_dir', None
        )

    @patch('kiwi.disk_format.DiskFormatVmdk')
    def test_disk_format_vmdk(self, mock_vmdk):
        xml_state = mock.Mock()
        DiskFormat('vmdk', xml_state, 'source_dir', 'target_dir')
        mock_vmdk.assert_called_once_with(
            xml_state, 'source_dir', 'target_dir', None
        )
