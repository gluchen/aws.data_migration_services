import boto3


class MyDms(object):
    def __init__(self):
        self.client = None # Default to None to fail nicely
        
    def initialize(self):
        """
        load the boto client.
        """
        self.client = boto3.client("dms")

    def describe_endpoints(self):
        """

        # Sample response
        
        {
          "Endpoints": [ 
            { 
              "CertificateArn": "string",
              "DatabaseName": "string",
              "EndpointArn": "string",
              "EndpointIdentifier": "string",
              "EndpointType": "string",
              "EngineName": "string",
              "ExtraConnectionAttributes": "string",
              "KmsKeyId": "string",
              "Port": number,
              "ServerName": "string",
              "SslMode": "string",
              "Status": "string",
              "Username": "string"
            }
          ],
          "Marker": "string"
        }

        """

    def list_task_ids(self):
        """
        List the tasks that it can read from the given account and so on

        use describe-instances command. http://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpoints.html



        ## Request Syntax:  # none are required
        
         
        {
          "Filters": [ 
            { 
                  "Name": "string",
                  "Values": [ "string" ]
            }
          ],
          "Marker": "string",
          "MaxRecords": number
        }


        ## Response Syntax

        {
           "Marker": "string",
           "ReplicationTasks": [ 
              { 
                 "LastFailureMessage": "string",
                 "MigrationType": "string",
                 "ReplicationInstanceArn": "string",
                 "ReplicationTaskArn": "string",
                 "ReplicationTaskCreationDate": number,
                 "ReplicationTaskIdentifier": "string",
                 "ReplicationTaskSettings": "string",
                 "ReplicationTaskStartDate": number,
                 "ReplicationTaskStats": { 
                    "ElapsedTimeMillis": number,
                    "FullLoadProgressPercent": number,
                    "TablesErrored": number,
                    "TablesLoaded": number,
                    "TablesLoading": number,
                    "TablesQueued": number
                 },
                 "SourceEndpointArn": "string",
                 "Status": "string",
                 "StopReason": "string",
                 "TableMappings": "string",
                 "TargetEndpointArn": "string"
              }
           ]
        }

        """
        assert self.client is not None
        instances = self.client.describe_replication_tasks()
        for task in replication_tasks:
            print task["ReplicationTaskCreationDate"]

        return instances

