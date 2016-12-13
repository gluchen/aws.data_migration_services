import unittest
import botocore.session
from botocore.stub import Stubber

import dms_task as dmt

class BT(unittest.TestCase):
    def setUp(self):
        self.MyDms = dmt.MyDms()
        # Normally, we would "self.MyDms.initialize()", but now we set theclient to a stub
        self.MyDms.client = botocore.session.get_session().create_client("dms", region_name="eu-central-1")
        self.stubber = Stubber(self.MyDms.client)



class test_it_can_list_tasks(BT):
    def test_empty_call_does_no_harm(self):
        response = {
           "Marker": "string",
           "ReplicationTasks": [ 
              { 
                 "LastFailureMessage": "string",
                 "MigrationType": "string",
                 "ReplicationInstanceArn": "string",
                 "ReplicationTaskArn": "string",
                 "ReplicationTaskCreationDate": 9999,
                 "ReplicationTaskIdentifier": "string",
                 "ReplicationTaskSettings": "string",
                 "ReplicationTaskStartDate": 9999,
                 "ReplicationTaskStats": { 
                    "ElapsedTimeMillis": 10,
                    "FullLoadProgressPercent": 100,
                    "TablesErrored": 0,
                    "TablesLoaded": 1,
                    "TablesLoading": 0,
                    "TablesQueued": 0
                 },
                 "SourceEndpointArn": "string",
                 "Status": "string",
                 "TableMappings": "string",
                 "TargetEndpointArn": "string"
              }
           ]
        }


        expected_params = {} # None Required
        self.stubber.add_response('describe_replication_tasks', response, expected_params)
        self.stubber.activate()

        #result = self.MyDms.client.describe_endpoints()
        result = self.MyDms.list_task_ids()
        assert result == response


if __name__ == "__main__":
    unittest.main()
