
class ebs_snapshot():

    def __init__(self, account_Id, account_name, volume_id, volume_name, region, refreshed_time, snapshot_age, status, reason):
        self.account_Id = account_Id
        self.account_name = account_name
        self.volume_id = volume_id
        self.volume_name = volume_name
        self.region = region
        self.refreshed_time = refreshed_time
        self.snapshot_age = snapshot_age
        self.status = status
        self.reason = reason
