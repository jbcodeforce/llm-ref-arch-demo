
## Amazon RDS Public Snapshots


### Description

 Checks the permission settings for your Amazon Relational Database Service (Amazon RDS) DB snapshots and alerts you if any snapshots are marked as public. When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot with particular users or accounts, mark the snapshot as private, and then specify the user or accounts you want to share the snapshot data with. Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.


### Alert Criteria




Red: The RDS  snapshot is marked as public.


### Recommended Action




Unless you are certain you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see Sharing a DB Snapshot or DB Cluster Snapshot. Note: For temporary technical reasons, items in this check cannot be excluded from view in the Trusted Advisor console.
To modify permissions for your snapshots directly, you can use a runbook in the AWS Systems Manager console. For more information, see AWSSupport-ModifyRDSSnapshotPermission.
 

### Additional Resources




Backing Up and Restoring Amazon RDS DB Instances

## ELB Security Groups


### Description

 Checks for load balancers configured with a missing security group or a security group that allows access to ports that are not configured for the load balancer. If a security group associated with a load balancer is deleted, the load balancer does not work as expected. If a security group allows access to ports that are not configured for the load balancer, the risk of loss of data or malicious attacks increases. 

### Alert Criteria


Yellow: The inbound rules of an Amazon VPC security group associated with a load balancer allow access to ports that are not defined in the load balancer's listener configuration. 
Red: A security group associated with a load balancer does not exist. 

### Recommended Action


Configure the security group rules to restrict access to only those ports and protocols that are defined in the load balancer listener configuration, plus the ICMP protocol to support Path MTU Discovery. See Listeners for Your Classic Load Balancer and Security Groups for Load Balancers in a VPC.
If a security group is missing, apply a new security group to the load balancer. Create security group rules that restrict access to only those ports and protocols that are defined in the load balancer listener configuration. See Security Groups for Load Balancers in a VPC. 

### Additional Resources


Elastic Load Balancing User Guide 
Configure Your Classic Load Balancer

## Auto Scaling Launch Configurations


### Description

 Checks for usage that is more than 80% of the Auto Scaling Launch Configurations Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Auto Scaling Limits

## Route 53 Traffic Policies


### Description

 Checks for usage that is more than 80% of the Route 53 Traffic Policies Limit per account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Route 53 Limits

## EBS Cold HDD (sc1) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS Cold HDD (sc1) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## Amazon Route 53 Failover Resource Record Sets


### Description

 Checks for Amazon Route 53 failover resource record sets that are misconfigured. When Amazon Route 53 health checks determine that the primary resource is unhealthy, Amazon Route 53 responds to queries with a secondary, backup resource record set. You must create correctly configured primary and secondary resource record sets for failover to work. Hosted zones created by AWS services won’t appear in your check results.


### Alert Criteria


Yellow: A primary failover resource record set does not have a corresponding secondary resource record set.
Yellow: A secondary failover resource record set does not have a corresponding primary resource record set.
Yellow: Primary and secondary resource record sets that have the same name are associated with the same health check.

### Recommended Action


If a failover resource set is missing, create the corresponding resource record set; see Creating Failover Resource Record Sets.
If your resource record sets are associated with the same health check, create separate health checks for each one; see Creating, Updating, and Deleting Health Checks.


Additional Information
Amazon Route 53 Health Checks and DNS Failover

## CloudFront Custom SSL Certificates in the IAM Certificate Store


### Description

 Checks the SSL certificates for CloudFront alternate domain names in the IAM certificate store and alerts you if the certificate is expired, will soon expire, uses outdated encryption, or is not configured correctly for the distribution. When a custom certificate for an alternate domain name expires, browsers that display your CloudFront content might show a warning message about the security of your website. Certificates that are encrypted by using the SHA-1 hashing algorithm are being deprecated by web browsers such as Chrome and Firefox.  If a certificate doesn't contain any domain names that match either Origin Domain Name or the domain name in the Host header of viewer requests, CloudFront returns an HTTP status code 502 (bad gateway) to the user. For more information, see Using Alternate Domain Names and HTTPS.

### Alert Criteria


Red: A custom SSL certificate is expired.
Yellow: A custom SSL certificate expires in the next seven days.
Yellow: A custom SSL certificate was encrypted by using the SHA-1 hashing algorithm.
Yellow: One or more of the alternate domain names in the distribution don't appear either in the Common Name field or the Subject Alternative Names field of the custom SSL certificate.

### Recommended Action


Renew an expired certificate or a certificate that is about to expire.
Replace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.
Replace the certificate with a certificate that contains the applicable values in the Common Name or Subject Alternative Domain Names fields.

### Additional Resources


Using an HTTPS Connection to Access Your Objects

## AWS Lambda Functions Using Deprecated Runtimes


### Description

 Checks for Lambda functions that are configured to use a runtime that is approaching deprecation or is deprecated. Deprecated runtimes are not eligible for security updates or technical support.
Notes:
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.
Published Lambda function versions are immutable, which means they can be invoked but not updated. Only the $LATEST version for a Lambda function can be updated. For more information, see Lambda function versions.

### Alert Criteria


Red: The function is running on a runtime that is already deprecated.
Yellow: The function is running on a runtime that will be deprecated within 120 days.

### Recommended Action


If you have functions that are running on a runtime that is approaching deprecation, you should prepare for migration to a supported runtime. For more information, see Runtime support policy.
We recommend that you delete earlier function versions that you’re no longer using.

### Additional Resources


Lambda runtimes

## AWS Lambda VPC-enabled Functions without Multi-AZ Redundancy


### Description

 Checks for VPC-enabled Lambda functions that are vulnerable to service interruption in a single availability zone. It is recommended for VPC-enabled functions to be connected to multiple availability zones for high availability.
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow: A VPC-enabled Lambda function connected to subnets in a single Availability Zone.

### Recommended Action


When configuring functions for access to your VPC, choose subnets in multiple Availability Zones to ensure high availability.

### Additional Resources


Configuring a Lambda function to access resources in a VPC
Resilience in AWS Lambda


## Neptune DB cluster snapshots should be encrypted at rest


### Description

 Checks if a Neptune DB cluster snapshot is encrypted at rest. The check fails if a Neptune DB cluster isn't encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: Neptune.6

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Neptune DB clusters should have IAM database authentication enabled


### Description

 Checks if a Neptune DB cluster has IAM database authentication enabled. The check fails if IAM database authentication isn't enabled for a Neptune DB cluster.

Source
AWS Security Hub
Security Hub Control Id: Neptune.7

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Neptune DB clusters should be configured to copy tags to snapshots


### Description

 Checks if a Neptune DB cluster is configured to copy tags to snapshots when the snapshots are created. The check fails if a Neptune DB cluster isn't configured to copy tags to snapshots.

Source
AWS Security Hub
Security Hub Control Id: Neptune.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB clusters should be encrypted at rest


### Description

 Checks if an RDS DB cluster is encrypted at rest. The check fails if an RDS DB cluster isn't encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: RDS.27

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Route 53 Name Server Delegations


### Description

 Checks for Amazon Route 53 hosted zones for which your domain registrar or DNS is not using the correct Route 53 name servers. When you create a hosted zone, Route 53 assigns a delegation set of four name servers. The names of these servers are ns-###.awsdns-##.com, .net, .org, and .co.uk, where ### and ## typically represent different numbers. Before Route 53 can route DNS queries for your domain, you must update your registrar's name server configuration to remove the name servers that the registrar assigned and add all four name servers in the Route 53 delegation set. For maximum availability, you must add all four Route 53 name servers. Hosted zones created by AWS services won’t appear in your check results.

### Alert Criteria


Yellow: A hosted zone for which the registrar for your domain does not use all four of the Route 53 name servers in the delegation set.

### Recommended Action


Add or update name server records with your registrar or with the current DNS service for your domain to include all four of the name servers in your Route 53 delegation set. To find these values, see Getting the Name Servers for a Hosted Zone. For information about adding or updating name server records, see Creating and Migrating Domains and Subdomains to Amazon Route&nbsp;53.

### Additional Resources


Working with Hosted Zones 


## EBS Magnetic (standard) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS Magnetic (standard) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## IAM Group


### Description

 Checks for usage that is more than 80% of the IAM Group Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## CloudFront Alternate Domain Names


### Description

 Checks Amazon CloudFront distributions for alternate domain names (CNAMES) that have incorrectly configured DNS settings. If a CloudFront distribution includes alternate domain names, the DNS configuration for the domains must route DNS queries to that distribution.

Note: This check assumes Amazon Route 53 DNS and Amazon CloudFront distribution are configured in the same AWS account. As such the Alert list may include resources otherwise working as expected due to DNS setting outsides of this AWS account.

### Alert Criteria


Yellow: A CloudFront distribution includes alternate domain names, but the DNS configuration is not correctly set up with a CNAME record or an Amazon Route 53 alias resource record.
Yellow: A CloudFront distribution includes alternate domain names, but Trusted Advisor could not evaluate the DNS configuration because there were too many redirects.
Yellow: A CloudFront distribution includes alternate domain names, but Trusted Advisor could not evaluate the DNS configuration for some other reason, most likely because of a timeout.

### Recommended Action


Update the DNS configuration to route DNS queries to the CloudFront distribution; see Using Alternate Domain Names (CNAMEs). If you're using Amazon Route 53 as your DNS service, see Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name. If the check timed out, try refreshing the check.

### Additional Resources


Amazon CloudFront Developer Guide

## Amazon EBS under-provisioned volumes


### Description

 Checks the Amazon Elastic Block Storage (Amazon EBS) volumes that were running at any time during the lookback period. This check alerts you if any EBS volumes were under-provisioned for your workloads. Consistent high utilization can indicate optimized, steady performance, but can also indicate that an application does not have enough resources.

Source
AWS Compute Optimizer

### Alert Criteria


Yellow: An EBS Volume that was under-provisioned during the lookback period. To determine if a volume is under-provisioned, we consider all default CloudWatch metrics (including IOPS and throughput). The algorithm used to identify under-provisioned EBS volumes follows AWS best practices. The algorithm is updated when a new pattern has been identified.

### Recommended Action


Consider upsizing volumes that have high utilization.

### Additional Resources


For more information about this recommendation, see the Trusted Advisor documentation.


## Amazon EBS over-provisioned volumes


### Description

 Checks the Amazon Elastic Block Storage (Amazon EBS) volumes that were running at any time during the lookback period. This check alerts you if any EBS volumes were over-provisioned for your workloads. When you have over-provisioned volumes, you’re paying for unused resources. Although some scenarios can result in low optimization by design, you can often lower your costs by changing the configuration of your EBS volumes. Estimated monthly savings are calculated by using the current usage rate for EBS volumes. Actual savings will vary if the volume isn’t present for a full month.

Source
AWS Compute Optimizer

### Alert Criteria


Yellow: An EBS Volume that was over-provisioned during the lookback period. To determine if a volume is over-provisioned, we consider all default CloudWatch metrics (including IOPS and throughput). The algorithm used to identify over-provisioned EBS volumes follows AWS best practices. The algorithm is updated when a new pattern has been identified.

### Recommended Action


Consider downsizing volumes that have low utilization.

### Additional Resources


For more information about this recommendation, see the Trusted Advisor documentation..


## RDS Cluster Parameter Groups


### Description

 Checks for usage that is more than 80% of the RDS Cluster Parameter Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## AWS Lambda under-provisioned functions for memory size


### Description

 Checks the AWS Lambda functions that were invoked at least once during the lookback period. This check alerts you if any of your Lambda functions were under-provisioned for memory size. When you have Lambda functions that are under-provisioned for memory size, these functions take longer time to complete.

Source
AWS Compute Optimizer

### Alert Criteria


Yellow: A Lambda function that was under-provisioned for memory size during the lookback period. To determine if a Lambda function is under-provisioned, we consider all default CloudWatch metrics for that function. The algorithm used to identify under-provisioned Lambda functions for memory size follows AWS best practices. The algorithm is updated when a new pattern has been identified.

### Recommended Action


Consider increasing the memory size of your Lambda functions.

### Additional Resources


For more information about this recommendation, see the Trusted Advisor documentation.


## AWS Lambda over-provisioned functions for memory size


### Description

 Checks the AWS Lambda functions that were invoked at least once during the lookback period. This check alerts you if any of your Lambda functions were over-provisioned for memory size. When you have Lambda functions that are over-provisioned for memory sizes, you’re paying for unused resources. Although some scenarios can result in low utilization by design, you can often lower your costs by changing the memory configuration of your Lambda functions. Estimated monthly savings are calculated by using the current usage rate for Lambda functions.

Source
AWS Compute Optimizer

### Alert Criteria


Yellow: A Lambda function that was over-provisioned for memory size during the lookback period. To determine if a Lambda function is over-provisioned, we consider all default CloudWatch metrics for that function. The algorithm used to identify over-provisioned Lambda functions for memory size follows AWS best practices. The algorithm is updated when a new pattern has been identified.

### Recommended Action


Consider reducing the memory size of your Lambda functions.

### Additional Resources


For more information about this recommendation, see the Trusted Advisor documentation page.


## Amazon RDS Multi-AZ


### Description

 Checks for DB instances that are deployed in a single Availability Zone. Multi-AZ deployments enhance database availability by synchronously replicating to a standby instance in a different Availability Zone. During planned database maintenance or the failure of a DB instance or Availability Zone, Amazon RDS automatically fails over to the standby so that database operations can resume quickly without administrative intervention. Because Multi-AZ deployments for the SQL Server engine use a different mechanism for synchronization, this check does not examine SQL Server instances.

### Alert Criteria


Yellow: A DB instance is deployed in a single Availability Zone.

### Recommended Action


If your application requires high availability, modify your DB instance to enable Multi-AZ deployment. See High Availability (Multi-AZ).

### Additional Resources


Regions and Availability Zones

## RDS Subnets per Subnet Group


### Description

 Checks for usage that is more than 80% of the RDS Subnets per Subnet Group Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## ELB Listener Security


### Description

 Checks for load balancers with listeners that do not use recommended security configurations for encrypted communication. AWS recommends using a secure protocol (HTTPS or SSL), up-to-date security policies, and ciphers and protocols that are secure.
When you use a secure protocol for a front-end connection (client to load balancer), the requests are encrypted between your clients and the load balancer, which is more secure.
Elastic Load Balancing provides predefined security policies  with ciphers and protocols that adhere to AWS security best practices. New versions of predefined policies are released as new configurations become available. 

### Alert Criteria


Yellow: A load balancer has no listener that uses a secure protocol (HTTPS or SSL). 
Yellow: A load balancer listener uses an outdated predefined SSL security policy. 
Yellow: A load balancer listener uses a cipher or protocol that is not recommended. 
Red: A load balancer listener uses an insecure cipher or protocol.

### Recommended Action


If the traffic to your load balancer must be secure, use either the HTTPS or the SSL protocol for the front-end connection.
Upgrade your load balancer to the latest version of the predefined SSL security policy. 
Use only the recommended ciphers and protocols. 
For more information, see Listener Configurations for Elastic Load Balancing.

### Additional Resources


Listener Configurations Quick Reference
Update SSL Negotiation Configuration of Your Load Balancer
SSL Negotiation Configurations for Elastic Load Balancing
SSL Security Policy Table


## Amazon EBS Public Snapshots


### Description

 Checks the permission settings for your Amazon Elastic Block Store (Amazon EBS) volume snapshots and alerts you if any snapshots are marked as public. When you make a snapshot public, you give all AWS accounts and users access to all the data on the snapshot. If you want to share a snapshot with particular users or accounts, mark the snapshot as private, and then specify the user or accounts you want to share the snapshot data with. Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.


### Alert Criteria




Red: The EBS volume snapshot is marked as public.


### Recommended Action




Unless you are certain you want to share all the data in the snapshot with all AWS accounts and users, modify the permissions: mark the snapshot as private, and then specify the accounts that you want to give permissions to. For more information, see Sharing an Amazon EBS Snapshot. Note: For temporary technical reasons, items in this check cannot be excluded from view in the Trusted Advisor console.
To modify permissions for your snapshots directly, you can use a runbook in the AWS Systems Manager console. For more information, see AWSSupport-ModifyEBSSnapshotPermission.
 

### Additional Resources




Amazon EBS Snapshots

## Amazon S3 Bucket Versioning


### Description

 Checks for Amazon Simple Storage Service buckets that do not have versioning enabled, or have versioning suspended. When versioning is enabled, you can easily recover from both unintended user actions and application failures. Versioning allows you to preserve, retrieve, and restore any version of any object stored in a bucket. You can use lifecycle rules to manage all versions of your objects as well as their associated costs by automatically archiving objects to the Glacier storage class or removing them after a specified time period. You can also choose to require multi-factor authentication (MFA) for any object deletions or configuration changes to your buckets. 

Versioning cannot be disabled after it has been enabled, but it can be suspended, which prevents new versions of objects from being created. Using versioning can increase your costs for Amazon S3, because you pay for storage of multiple versions of an object.

### Alert Criteria


Green: Versioning is enabled for the bucket.
Yellow: Versioning is not enabled for the bucket.
Yellow: Versioning is suspended for the bucket.

### Recommended Action


Enable bucket versioning on most buckets to prevent accidental deletion or overwriting. See Using Versioning and Enabling Versioning Programmatically. 

If bucket versioning is suspended, consider reenabling versioning. For information on working with objects in a versioning-suspended bucket, see Managing Objects in a Versioning-Suspended Bucket.

When versioning is enabled or suspended, you can define lifecycle configuration rules to mark certain object versions as expired or to permanently remove unneeded object versions. For more information, see Object Lifecycle Management. 

MFA Delete requires additional authentication when the versioning status of the bucket is changed or when versions of an object are deleted. It requires the user to enter credentials and a code from an approved authentication device. For more information, see MFA Delete.

### Additional Resources


Working with Buckets

## AWS Well-Architected high risk issues for performance efficiency


### Description

 Checks for high risk issues (HRIs) for your workloads in the performance pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.

### Alert Criteria


Red: At least one active high risk issue was identified in the performance pillar for AWS Well-Architected.
Green: No active high risk issues were detected in the performance pillar for AWS Well-Architected.

### Recommended Action


AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the AWS Well-Architected tool to review your answers and take action to resolve your active issues.

## ELB Network Load Balancers


### Description

 Checks for usage that is more than 80% of the ELB Network Load Balancers Limit. Classic Load Balancers and Application Load Balancers have separate limits. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


AWS Service Limits - Elastic Load Balancing default service limits

## AWS Well-Architected high risk issues for security


### Description

 Checks for high risk issues (HRIs) for your workloads in the security pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.

### Alert Criteria


Red: At least one active high risk issue was identified in the security pillar for AWS Well-Architected.
Green: No active high risk issues were detected in the security pillar for AWS Well-Architected.

### Recommended Action


AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the AWS Well-Architected tool to review your answers and take action to resolve your active issues.

## AWS Well-Architected high risk issues for reliability


### Description

 Checks for high risk issues (HRIs) for your workloads in the Reliability pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.

### Alert Criteria


Red: At least one active high risk issue was identified in the reliability pillar for AWS Well-Architected.
Green: No active high risk issues were detected in the reliability pillar for AWS Well-Architected.

### Recommended Action


AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the AWS Well-Architected tool to review your answers and take action to resolve your active issues.

## AWS Well-Architected high risk issues for cost optimization


### Description

 Checks for high risk issues (HRIs) for your workloads in the cost optimization pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.

### Alert Criteria


Red: At least one active high risk issue was identified in the cost optimization pillar for AWS Well-Architected.
Green: No active high risk issues were detected in the cost optimization pillar for AWS Well-Architected.

### Recommended Action


AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the AWS Well-Architected tool to review your answers and take action to resolve your active issues.

## Amazon RDS Backups


### Description

 Checks for automated backups of Amazon RDS DB instances. By default, backups are enabled with a retention period of 1 day. Backups reduce the risk of unexpected data loss and allow for point-in-time recovery.

### Alert Criteria


Red: A DB instance has the backup retention period set to 0 days.

### Recommended Action


Set the retention period for the automated DB instance backup to 1 to 35 days as appropriate to the requirements of your application. See Working With Automated Backups.

### Additional Resources


Getting Started with Amazon RDS

## AWS Lambda Functions with High Error Rates


### Description

 Checks for Lambda functions with high error rates that may result in high cost. Lambda charges based on the number of requests and aggregate execution time for your function. Function errors may cause retries that incur additional charges.
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow: Functions where > 10% of invocations end in error on any given day within the last 7 days.

### Recommended Action


Consider the following guidelines to reduce errors. Function errors include errors returned by the function's code and errors returned by the function's runtime. To help you troubleshoot Lambda errors, Lambda integrates with services like Amazon CloudWatch and AWS X-Ray. You can use a combination of logs, metrics, alarms, and X-ray tracing to quickly detect and identify issues in your function code, API, or other resources that support your application. For more information, see Monitoring and troubleshooting Lambda applications. For more information on handling errors with specific runtimes, see Error handling and automatic retries in AWS Lambda. For additional troubleshooting, see Troubleshooting issues in Lambda.You can also choose from an ecosystem of monitoring and observability tools provided by AWS Lambda partners. For additional information about Partners, see AWS Lambda Partners.

### Additional Resources


Error Handling and Automatic  Retries in AWS Lambda
Monitoring and Troubleshooting Lambda applications
Lambda Function Retry Timeout SDK
Troubleshooting  issues in Lambda
API Invoke Errors
Error Processor Sample Application for AWS Lambda


## AWS Lambda Functions with Excessive Timeouts


### Description

 Checks for Lambda functions with high timeout rates that may result in high cost. Lambda charges based on execution time for your function and number of requests for your function. Function timeouts result in function errors that may cause retries that incur additional request and execution time charges.
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow: Functions where > 10% of invocations end in an error due to a timeout on any given day within the last 7 days.

### Recommended Action


Inspect function logging and X-ray traces to determine the contributor to the high function duration. Implement logging in your code at relevant parts, such as before or after API calls or database connections. By default, AWS SDK clients timeouts may be longer than the configured function duration. Adjust API and SDK connection clients to retry or fail within the function timeout. If the expected duration is longer than the configured timeout, you can increase the timeout setting for the function. For more information, see Monitoring and troubleshooting Lambda applications.

### Additional Resources


Monitoring and troubleshooting Lambda applications
Lambda Function Retry Timeout SDK
Using AWS Lambda with AWS X-Ray
Accessing Amazon CloudWatch logs for AWS Lambda
Error Processor Sample Application for AWS Lambda


## AWS CloudTrail Logging


### Description

 Checks for your use of AWS CloudTrail. CloudTrail provides increased visibility into activity in your AWS account by recording information about AWS API calls made on the account. You can use these logs to determine, for example, what actions a particular user has taken during a specified time period or which users have taken actions on a particular resource during a specified time period. Because CloudTrail delivers log files to an Amazon Simple Storage Service (Amazon S3) bucket, CloudTrail must have write permissions for the bucket. If a trail applies to all regions (the default when creating a new trail), the trail appears multiple times in the Trusted Advisor report.

### Alert Criteria


Yellow: CloudTrail reports log delivery errors for a trail.
Red: A trail has not been created for a region, or logging is turned off for a trail.

### Recommended Action


To create a trail and start logging from the console, go to the AWS CloudTrail console. 
To start logging, see Stopping and Starting Logging for a Trail. 
If you receive log delivery errors, check to make sure that the bucket exists and that the necessary policy is attached to the bucket; see Amazon S3 Bucket Policy.

### Additional Resources


AWS CloudTrail User Guide
Supported Regions
Supported Services

## RDS Cluster Roles


### Description

 Checks for usage that is more than 80% of the RDS Cluster Roles Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Route 53 Max Health Checks


### Description

 Checks for usage that is more than 80% of the Route 53 Health Checks Limit per account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Route 53 Limits

## RDS DB Manual Snapshots


### Description

 Checks for usage that is more than 80% of the RDS DB Manual Snapshots Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon Aurora DB Instance Accessibility


### Description

 Checks for cases where an Amazon Aurora DB cluster has both private and public instances. When your primary instance fails, a replica can be promoted to a primary instance. If that replica is private, users who have only public access would no longer be able to connect to the database after failover. It's best practice for all the DB instances in a cluster to have the same accessibility.

### Alert Criteria


Yellow: The instances in an Aurora DB cluster have different accessibility (a mix of public and private).

### Recommended Action


Modify the Publicly Accessible setting of the instances in the DB cluster so that they are all either public or private. For details, see the instructions for MySQL instances at Modifying a DB Instance Running the MySQL Database Engine.

### Additional Resources


Fault Tolerance for an Aurora DB Cluster

## AWS Direct Connect Connection Redundancy


### Description

 Checks for regions that have only one AWS Direct Connect connection. Connectivity to your AWS resources should have two Direct Connect connections configured at all times to provide redundancy in case a device is unavailable.
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow:  The region has only one Direct Connect connection.

### Recommended Action


Configure an additional Direct Connect connection in this region to protect against device unavailability. For more information, see Configure Redundant Connections with AWS Direct Connect. To protect against site unavailability and add location redundancy, configure the additional Direct Connect connection to a different Direct Connect location.

### Additional Resources


Getting Started with AWS Direct Connect
AWS Direct Connect FAQs 

## AWS Resilience Hub resilience scores


### Description

 Checks if you have run an assessment for your applications in Resilience Hub. This check alerts you if your resilience scores are below a specific value. Results for this check are automatically refreshed once every day.

### Alert Criteria


Green: Your application has a resilience score of 70 or greater.
Yellow: Your application has a resilience score of 40 through 69.
Yellow: The application hasn't been assessed yet.
Red: Your application has a resilience score of less than 40.

### Recommended Action


Sign in to the Resilience Hub console and run an assessment for your application. Review
 the recommendations to improve the resilience score.

Additional Information
Resilience Hub concepts


## AWS Resilience Hub policy breached


### Description

 Checks Resilience Hub for applications that don't meet the recovery time objective (RTO) and 
recovery point objective (RPO) that the policy defines. The check alerts you if your application 
doesn't meet the RTO and RPO objectives you've set for an application in Resilience Hub.

### Alert Criteria


Green: The application has a policy and meets the RTO and RPO objectives.
Yellow: The application hasn't been assessed yet.
Red: The application has a policy but doesn't meet the RTO and RPO objectives.

### Recommended Action


Sign in to the Resilience Hub console and review the recommendations, so that your 
application meets the RTO and RPO objectives.

Additional Information
Resilience Hub concepts


## AWS Resilience Hub assessment age


### Description

 Checks how long since you last ran an application assessment. This check alerts you if you haven’t run an application assessment for a specified number of days.

### Alert Criteria


Green: Your application assessment ran in the last 30 days.
Yellow: Your application assessment hasn't run in the last 30 days.

### Recommended Action


Sign in to the Resilience Hub console and run an assessment for your application.

### Additional Resources


Resilience Hub concepts

## AWS CloudHSM clusters running HSM instances in a single AZ


### Description

 Checks your clusters that run HSM instances in a single Availability Zone (AZ). This check alerts you if your clusters are at risk of not having the most recent backup.

### Alert Criteria


Yellow: A CloudHSM cluster is running all HSM instances in a single Availability Zone for more than 1 hour.
Green: A CloudHSM cluster is running all HSM instances in at least two different Availability Zones.

### Recommended Action


Create at least one more instance for the cluster in a different Availability Zone.

Additional Information
Best practices for AWS CloudHSM


## IAM Access Key Rotation


### Description

 Checks for active IAM access keys that have not been rotated in the last 90 days.  When you rotate your access keys regularly, you reduce the chance that a compromised key could be used without your knowledge to access resources. For the purposes of this check, the last rotation date and time is when the access key was created or most recently activated. The access key number and date come from the access_key_1_last_rotated and access_key_2_last_rotated information in the most recent IAM credential report. Because the regeneration frequency of a credential report  is restricted, refreshing this check might not reflect recent changes (for details, see Getting Credential Reports for Your AWS Account).
In order to create and rotate access keys, a user must have the appropriate permissions. For more information, see Allow Users to Manage Their Own Passwords, Access Keys, and SSH Keys.

### Alert Criteria


Green: The access key is active and has been rotated in the last 90 days.
Yellow: The access key is active and has been rotated in the last 2 years, but more than 90 days ago.
Red: The access key is active and has not been rotated in the last 2 years.

### Recommended Action


Rotate access keys on a regular basis. See Rotating Access Keys and Managing Access Keys for IAM Users.

### Additional Resources


IAM Best Practices
How to rotate access keys for IAM users (AWS blog)

## MFA on Root Account


### Description

 Checks the root account and warns if multi-factor authentication (MFA) is not enabled. For increased security, we recommend that you protect your account by using MFA, which requires a user to enter a unique authentication code from their MFA hardware or virtual device when interacting with the AWS console and associated websites.


### Alert Criteria


Red: MFA is not enabled on the root account.


### Recommended Action


Log in to your root account and activate an MFA device. See Checking MFA Status and Setting Up an MFA Device.


### Additional Resources


Using Multi-Factor Authentication (MFA) Devices with AWS

## Large Number of Rules in an EC2 Security Group


### Description

 Checks each Amazon Elastic Compute Cloud (EC2) security group for an excessive number of rules. If a security group has a large number of rules, performance can be degraded.

For more information, see Amazon EC2 Security Groups.


### Alert Criteria



Yellow: An Amazon EC2-VPC security group has more than 50 rules.

Yellow: An Amazon EC2-Classic security group has more than 100 rules.


### Recommended Action



Reduce the number of rules in a security group by deleting unnecessary or overlapping rules. For more information, see Deleting Rules from a Security Group.


### Additional Resources



Amazon EC2 Security Groups

## VPC Internet Gateways


### Description

 Checks for usage that is more than 80% of the VPC Internet Gateways Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


VPC Gateway Limits

## Security Groups - Specific Ports Unrestricted


### Description

 Checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data). The ports with highest risk are flagged red, and those with less risk are flagged yellow. Ports flagged green are typically used by applications that require unrestricted access, such as HTTP and SMTP.

If you have intentionally configured your security groups in this manner, we recommend using additional security measures to secure your infrastructure (such as IP tables).

Note: This check only evaluates security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Services are flagged as red or yellow, but they don’t pose a security risk and can be safely ignored or excluded. For more information, see the Trusted Advisor FAQ.


### Alert Criteria



Green: Access to port 80, 25, 443, or 465 is unrestricted.
Red: Access to port 20, 21, 1433, 1434, 3306, 3389, 4333, 5432, or 5500 is unrestricted.
Yellow: Access to any other port is unrestricted.


### Recommended Action



Restrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.

### Additional Resources


Amazon EC2 Security Groups
List of TCP and UDP port numbers (Wikipedia)
Classless Inter-Domain Routing (Wikipedia)

## Amazon S3 Bucket Permissions


### Description

 Checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions or allow access to any authenticated AWS user. Bucket permissions that grant List access can result in higher than expected charges if objects in the bucket are listed by unintended users at a high frequency. Bucket permissions that grant Upload/Delete access create potential security vulnerabilities by allowing users that to add, modify, or remove items in a bucket.

### Alert Criteria


Yellow: The bucket ACL allows List access for "Everyone" or "Any Authenticated AWS User".
Yellow: A bucket policy allows any kind of open access.
Yellow: Bucket policy has statements that grant public access. The “Block public and cross-account access to buckets that have public policies” setting is turned on and has restricted access to only authorized users of that account until public statements are removed.
Yellow: Trusted Advisor does not have permission to check the policy, or the policy could not be evaluated for other reasons.
Red: The bucket ACL allows Upload/Delete access for "Everyone" or "Any Authenticated AWS User".

### Recommended Action


If a bucket allows open access, determine if open access is truly needed. If not, update the bucket permissions to restrict access to the owner or specific users. Use Amazon S3 Block Public Access to control the settings that allow public access to your data. See Setting Bucket and Object Access Permissions.

### Additional Resources


Managing Access Permissions to Your Amazon S3 Resources

## RDS cluster snapshots and database snapshots should be encrypted at rest


### Description

 Checks if Amazon RDS cluster snapshots and database snapshots are encrypted.

Source
AWS Security Hub
Security Hub control ID: RDS.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB Instances should prohibit public access, determined by the PubliclyAccessible configuration


### Description

 Checks if RDS instances are publicly accessible by evaluating the publiclyAccessible field in the instance configuration item.

Source
AWS Security Hub
Security Hub control ID: RDS.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB instances should have encryption at-rest enabled


### Description

 Checks if storage encryption is enabled for your RDS DB instances.

Source
AWS Security Hub
Security Hub control ID: RDS.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS snapshot should be private


### Description

 Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public.

Source
AWS Security Hub
Security Hub control ID: RDS.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should have origin access identity enabled


### Description

 Checks if an Amazon CloudFront distribution with an Amazon S3 origin type has Origin Access Identity (OAI) configured. The check fails if the CloudFront distribution that is backed by Amazon S3 does not have OAI configured.

Source
AWS Security Hub
Security Hub control ID: CloudFront.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS Config should be enabled


### Description

 Checks if the Config service is enabled in the account for the local region and is recording all resources.

Source
AWS Security Hub
Security Hub control ID: Config.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Route 53 Alias Resource Record Sets


### Description

 Checks for resource record sets that can be changed to alias resource record sets to improve performance and save money. An alias resource record set routes DNS queries to an AWS resource (for example, an Elastic Load Balancing load balancer or an Amazon S3 bucket) or to another Route 53 resource record set. When you use alias resource record sets, Route 53 routes your DNS queries to AWS resources free of charge. Hosted zones created by AWS services won’t appear in your check results.

### Alert Criteria


Yellow: A resource record set is a CNAME to an Amazon S3 website.
Yellow: A resource record set is a CNAME to an Amazon CloudFront distribution.
Yellow: A resource record set is a CNAME to an Elastic Load Balancing load balancer.

### Recommended Action


Replace the listed CNAME resource record sets with alias resource record sets; see Choosing Between Alias and Non-Alias Resource Record Sets. You also need to change the record type from CNAME to A or AAAA, depending on the AWS resource; see Values that You Specify When You Create or Edit Amazon Route 53 Resource Record Sets.

### Additional Resources


Routing Queries to AWS Resources

## Amazon Elasticsearch Service domains should have encryption at-rest enabled


### Description

 Checks whether Amazon Elasticsearch Service domains have encryption at rest configuration enabled. This check fails if the EncryptionAtRestOptions field is not enabled.

Source
AWS Security Hub
Security Hub control ID: ES.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB instances should have deletion protection enabled


### Description

 Checks if RDS DB instances have deletion protection enabled.

Source
AWS Security Hub
Security Hub control ID: RDS.8

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Security Groups - Unrestricted Access


### Description

 Checks security groups for rules that allow unrestricted access to a resource. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data).

Note: This check only evaluates security groups that you create and their inbound rules for IPv4 addresses. Security groups created by AWS Directory Services are flagged as red or yellow, but they don’t pose a security risk and can be safely ignored or excluded. For more information, see the Trusted Advisor FAQ.


### Alert Criteria



Red: A security group rule has a source IP address with a /0 suffix for ports other than 25, 80, or 443.


### Recommended Action



Restrict access to only those IP addresses that require it. To restrict access to a specific IP address, set the suffix to /32 (for example, 192.0.2.10/32). Be sure to delete overly permissive rules after creating rules that are more restrictive.


### Additional Resources


Amazon EC2 Security Groups
Classless Inter-Domain Routing (Wikipedia)

## RDS clusters should have deletion protection enabled


### Description

 Checks if RDS clusters have deletion protection enabled.

Source
AWS Security Hub
Security Hub control ID: RDS.7

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon RDS Security Group Access Risk


### Description

 Checks security group configurations for Amazon Relational Database Service (Amazon RDS) and warns when a security group rule might grant overly permissive access to your database. Recommended configuration for any security group rule is to allow access from specific Amazon Elastic Compute Cloud (Amazon EC2) security groups or from a specific IP address.


### Alert Criteria


Yellow: A DB security group rule references an Amazon EC2 security group that grants global access on one of these ports: 20, 21, 22, 1433, 1434, 3306, 3389, 4333, 5432, 5500.

Yellow: A DB security group rule grants access to more than a single IP address (the CIDR rule suffix is not /0 or /32).

Red: A DB security group rule grants global access (the CIDR rule suffix is /0).


### Recommended Action


Review your security group rules and restrict access to authorized IP addresses or IP ranges. To edit a security group, use the AuthorizeDBSecurityGroupIngress API or the AWS Management Console. For more information, see Working with DB Security Groups.


### Additional Resources


Amazon RDS Security Groups
Classless Inter-Domain Routing
List of TCP and UDP port numbers

## GuardDuty should be enabled


### Description

 Checks if Amazon GuardDuty is enabled in your AWS account and region.

Source
AWS Security Hub
Security Hub control ID: GuardDuty.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Enhanced monitoring should be configured for RDS DB instances


### Description

 Checks if enhanced monitoring is enabled for your RDS DB instances.

Source
AWS Security Hub
Security Hub control ID: RDS.6

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon EC2 Reserved Instance Lease Expiration


### Description

 Checks for Amazon EC2 Reserved Instances that are scheduled to expire within the next 30 days or have expired in the preceding 30 days. Reserved Instances do not renew automatically; you can continue using an EC2 instance covered by the reservation without interruption, but you will be charged On-Demand rates. New Reserved Instances can have the same parameters as the expired ones, or you can purchase Reserved Instances with different parameters.


The estimated monthly savings we show is the difference between the On-Demand and Reserved Instance rates for the same instance type.


### Alert Criteria




Yellow: The Reserved Instance lease expires in less than 30 days.


Yellow: The Reserved Instance lease expired in the preceding 30 days.


### Recommended Action




Consider purchasing a new Reserved Instance to replace the one that is nearing the end of its term. For more information, see How to Purchase Reserved Instances and Buying Reserved Instances.
 

### Additional Resources




Reserved Instances


Instance Types

## Amazon Route 53 High TTL Resource Record Sets


### Description

 Checks for resource record sets that can benefit from having a lower time-to-live (TTL) value. TTL is the number of seconds that a resource record set is cached by DNS resolvers. When you specify a long TTL, DNS resolvers take longer to request updated DNS records, which can cause unnecessary delay in rerouting traffic (for example, when DNS Failover detects and responds to a failure of one of your endpoints). Hosted zones created by AWS services won’t appear in your check results.

### Alert Criteria


Yellow: A resource record set whose routing policy is Failover has a TTL greater than 60 seconds.
Yellow: A resource record set with an associated health check has a TTL greater than 60 seconds.

### Recommended Action


Enter a TTL value of 60 seconds for the listed resource record sets. For more information, see Working with Resource Record Sets.

### Additional Resources


Amazon Route&nbsp;53 Health Checks and DNS Failover

## DynamoDB Read Capacity


### Description

 Checks for usage that is more than 80% of the DynamoDB Provisioned Throughput Limit for Reads per Account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


DynamoDB Limits

## Database logging should be enabled


### Description

 Checks if the following Amazon RDS logs are enabled and sent to CloudWatch Logs: Oracle: (Alert, Audit, Trace, Listener), PostgreSQL: (Postgresql, Upgrade), MySQL: (Audit, Error, General, SlowQuery), MariaDB: (Audit, Error, General, SlowQuery), SQL Server: (Error, Agent), Aurora: (Audit, Error, General, SlowQuery), Aurora-MySQL: (Audit, Error, General, SlowQuery), Aurora-PostgreSQL: (Postgresql).

Source
AWS Security Hub
Security Hub control ID: RDS.9

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## NAT Gateway AZ Independence


### Description

 Checks if your NAT Gateways are configured with Availability Zone (AZ) independence.
A NAT Gateway enables resources in your private subnet to securely connect to services outside the subnet using the NAT
Gateway’s IP addresses and drops any unsolicited inbound traffic. Each NAT Gateway operates within a designated
Availability Zone (AZ) and is built with redundancy in that AZ only. Therefore, your resources in a particular AZ should use a
NAT Gateway in the same AZ so that any potential outage of a NAT Gateway or its AZ does not impact your resources in
another AZ.

### Alert Criteria


Red: Traffic from your subnet in one AZ is being routed through a NATGW in a different AZ
Green: Traffic from your subnet in one AZ is being routed through a NATGW in the same AZ

### Recommended Action


Please check the AZ of your subnet and route traffic through a NAT Gateway in the same AZ.
If there is no NATGW in the AZ, please create one and then route your subnet traffic through it.
If you have the same route table associated across subnets in different AZs, keep this route table associated to the subnets
that reside in the same AZ as the NAT Gateway and for subnets in the other AZ, please associate a separate route table
with a route to a NAT Gateway in this other AZ.
We recommend choosing a maintenance window for architecture changes in your Amazon VPC.

### Additional Resources



Please refer to the AWS Public documentation on:How to create a NAT GatewayHow to configure routes for different NAT Gateway use cases Hub conceptsReach out to AWS Support for additional help

## Single AZ Application Check


### Description

 Checks through network patterns if your egress network traffic is routing through a single Availability Zone (AZ).

An AZ is a distinct location that is insulated from any impact in other zones. By spreading your service across multiple AZs, you limit the blast radius of an AZ failure.

### Alert Criteria


Yellow: Your application may be deployed in only one AZ based on observed egress network patterns. If this is true
and your application expects high availability, we recommend that you provision your application resources and
implement your network flows to utilize multiple Availability Zones.

### Recommended Action


If your application requires high availability, consider implementing a multi-AZ architecture for higher availability.

## RDS DB Instances


### Description

 Checks for usage that is more than 80% of the RDS DB Instances Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon EC2 Availability Zone Balance


### Description

 Checks the distribution of Amazon Elastic Compute Cloud (Amazon EC2) instances across Availability Zones in a region. Availability Zones are distinct locations that are designed to be insulated from failures in other Availability Zones and to provide inexpensive, low-latency network connectivity to other Availability Zones in the same region. By launching instances in multiple Availability Zones in the same region, you can help protect your applications from a single point of failure.

### Alert Criteria


Yellow: The region has instances in multiple zones, but the distribution is uneven (the difference between the highest and lowest instance counts in utilized Availability Zones is greater than 20%).
Red: The region has instances only in a single Availability Zone.

### Recommended Action


Balance your Amazon EC2 instances evenly across multiple Availability Zones. You can do this by launching instances manually or by using Auto Scaling to do it automatically. For more information, see Launch Your Instance and Load Balance Your Auto Scaling Group.

### Additional Resources


Auto Scaling Getting Started Guide
Auto Scaling Developer Guide

## ElastiCache clusters should not use the default subnet group


### Description

 Checks if ElastiCache clusters are configured with a custom subnet group. The check fails for an ElastiCache cluster if 'CacheSubnetGroupName' has the value 'default'.

Source
AWS Security Hub
Security Hub Control Id: ElastiCache.7

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Elastic Beanstalk should stream logs to CloudWatch


### Description

 Checks if an AWS Elastic Beanstalk environment is configured to send logs to CloudWatch Logs. The check fails if the Elastic Beanstalk environment is not configured to send logs to CloudWatch Logs.

Source
AWS Security Hub
Security Hub Control Id: ElasticBeanstalk.3

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 Block Public Access setting should be enabled


### Description

 Checks if the following public access block settings are configured from account level: ignorePublicAcls: True, blockPublicPolicy: True, blockPublicAcls: True, restrictPublicBuckets: True.

Source
AWS Security Hub
Security Hub control ID: S3.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Redshift clusters should be encrypted at rest


### Description

 Checks if an Amazon Redshift cluster is encrypted at rest. The check fails if a Redshift cluster isn't encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: Redshift.10

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should prohibit public read access


### Description

 Checks if your S3 buckets allow public read access by evaluating the Block Public Access settings, the bucket policy, and the bucket access check list (ACL).

Source
AWS Security Hub
Security Hub control ID: S3.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Step Functions state machines should have logging turned on


### Description

 This controls assesses if an AWS Step Functions state machine has logging turned on. The check fails if a state machine doesn't have logging turned on.

Source
AWS Security Hub
Security Hub Control Id: StepFunctions.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should prohibit public write access


### Description

 Checks if your S3 buckets allow public write access by evaluating the Block Public Access settings, the bucket policy, and the bucket access check list (ACL).

Source
AWS Security Hub
Security Hub control ID: S3.3

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Athena workgroups should be encrypted at rest


### Description

 Checks if an Athena workgroup is encrypted at rest. The check fails if an Athena workgroup isn’t encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: Athena.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 Block Public Access setting should be enabled at the bucket-level


### Description

 Checks if Amazon S3 buckets have bucket level public access blocks applied. This check fails if any of the bucket level settings are set to "false" public: ignorePublicAcls, blockPublicPolicy, blockPublicAcls, restrictPublicBuckets.

Source
AWS Security Hub
Security Hub control ID: S3.8

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECS service using a single AZ


### Description

 Checks that your service configuration uses a single Availability Zone (AZ).
An AZ is a distinct location that is insulated from failures in other zones. This supports inexpensive, low-latency network connectivity between AZs in the same AWS Region. By launching instances in multiple AZs in the same Region, you can help protect your applications from a single point of failure.

### Alert Criteria


Yellow: An Amazon ECS service is running all tasks in a single AZ.
Green: An Amazon ECS service is running tasks in at least two different AZs.

### Recommended Action


Create at least one more task for the service in a different AZ.

### Additional Resources


Amazon ECS capacity and availability

## Amazon DocumentDB clusters should be encrypted at rest


### Description

 Checks if an Amazon DocumentDB cluster is encrypted at rest. The check fails if an Amazon DocumentDB cluster isn't encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: DocumentDB.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CodeBuild GitHub or Bitbucket source repository URLs should use OAuth


### Description

 Checks if the GitHub or Bitbucket source repository URL contains either personal access tokens or user name and password.

Source
AWS Security Hub
Security Hub control ID: CodeBuild.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECS Multi-AZ placement strategy


### Description

 Checks that your Amazon ECS service uses the spread placement strategy based on availability zone. This strategy distributes tasks across Availability Zones (AZs) in the same AWS Region and can help protect your applications from a single point of failure.
For tasks that run as part of an Amazon ECS service, spread is the default task placement strategy.
This check also verifies that spread is the first or only strategy in your list of enabled placement strategies.

### Alert Criteria


Yellow: Spread by availability zone is disabled or isn't the first strategy in your list of enabled placement strategies for your Amazon ECS service.
Green: Spread by availability zone is the first strategy in your list of enabled placement strategies or the only placement strategy enabled for your Amazon ECS service.

### Recommended Action


 Enable the spread task placement strategy to distribute tasks across multiple AZs. Verify that spread by availability zone is the first strategy for all enabled task placement strategies or the only strategy used. If you choose to manage AZ placement, you can use a mirrored service in another AZ to mitigate these risks.

### Additional Resources


Amazon ECS task placement strategies

## Neptune DB clusters should be encrypted at rest


### Description

 Checks if a Neptune DB cluster is encrypted at rest. The check fails if a Neptune DB cluster isn't encrypted at rest.

Source
AWS Security Hub
Security Hub Control Id: Neptune.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CodeBuild project environment variables should not contain clear text credentials


### Description

 Checks if the project contains environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

Source
AWS Security Hub
Security Hub control ID: CodeBuild.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Neptune DB clusters should publish audit logs to CloudWatch Logs


### Description

 Checks if a Neptune DB cluster publishes audit logs to Amazon CloudWatch Logs. The check fails if a Neptune DB cluster doesn't publish audit logs to CloudWatch Logs. `EnableCloudWatchLogsExport` should be set to Audit.

Source
AWS Security Hub
Security Hub Control Id: Neptune.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ACM certificates should be renewed after a specified time period


### Description

 Checks if ACM Certificates in your account are marked for expiration within a specified time period. Certificates provided by ACM are automatically renewed. ACM does not automatically renew certificates that you import.

Source
AWS Security Hub
Security Hub control ID: ACM.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Auto Scaling Group Health Check


### Description

 Examines the health check configuration for Auto Scaling groups. If Elastic Load Balancing is being used for an Auto Scaling group, the recommended configuration is to enable an Elastic Load Balancing health check. If an Elastic Load Balancing health check is not used, Auto Scaling can only act upon the health of the Amazon Elastic Compute Cloud (Amazon EC2) instance and not on the application that is running on the instance.

### Alert Criteria


Yellow: An Auto Scaling group has an associated load balancer, but the Elastic Load Balancing health check is not enabled.
Yellow: An Auto Scaling group does not have an associated load balancer, but the Elastic Load Balancing health check is enabled.

### Recommended Action


If the Auto Scaling group has an associated load balancer, but the Elastic Load Balancing health check is not enabled, see Add an Elastic Load Balancing Health Check to your Auto Scaling Group.
If the Elastic Load Balancing health check is enabled, but no load balancer is associated with the Auto Scaling group, see Set Up an Auto-Scaled and Load-Balanced Application.

### Additional Resources


Auto Scaling Developer Guide

## EC2-Classic Elastic IP Addresses


### Description

 Checks for usage that is more than 80% of the EC2-Classic Elastic IP Addresses Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EC2 Limits

## EBS Throughput Optimized HDD (st1) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS Throughput Optimized HDD (st1) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## ELB Classic Load Balancers


### Description

 Checks for usage that is more than 80% of the ELB Classic Load Balancers. Application Load Balancers and Network Load Balancers have a separate limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


AWS Service Limits - Elastic Load Balancing default service limits

## Underutilized Amazon EBS Volumes


### Description

 Checks Amazon Elastic Block Store (Amazon EBS) volume configurations and warns when volumes appear to be underused. Charges begin when a volume is created. If a volume remains unattached or has very low write activity (excluding boot volumes) for a period of time, the volume is probably not being used.

### Alert Criteria


Yellow: A volume is unattached or had less than 1 IOPS per day for the past 7 days.

### Recommended Action


Consider creating a snapshot and deleting the volume to reduce costs. For more information, see Creating an Amazon EBS Snapshot and Deleting an Amazon EBS Volume.

### Additional Resources


Amazon Elastic Block Store (Amazon EBS)
Monitoring the Status of Your Volumes

## RDS Read Replicas per Master


### Description

 Checks for usage that is more than 80% of the RDS Read Replicas per Master Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## IAM Policies


### Description

 Checks for usage that is more than 80% of the IAM Policies Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## EBS Active Snapshots


### Description

 Checks for usage that is more than 80% of the EBS Active Snapshots Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## ElastiCache replication groups should have encryption-at-rest enabled


### Description

 Checks if ElastiCache replication groups have encryption-at-rest enabled. This check fails if encryption-at-rest is not enabled for a ElastiCache replication group.

Source
AWS Security Hub
Security Hub Control Id: ElastiCache.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## An RDS event notifications subscription should be configured for critical cluster events


### Description

 Checks if an Amazon RDS Event subscription for RDS clusters is configured to notify on event categories of both "maintenance" and "failure".

Source
AWS Security Hub
Security Hub control ID: RDS.19

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ElastiCache replication groups should have encryption-in-transit enabled


### Description

 Checks if ElastiCache replication groups have encryption-in-transit enabled. This check fails if encryption-in-transit is not enabled for a ElastiCache replication group.

Source
AWS Security Hub
Security Hub Control Id: ElastiCache.5

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should have server-side encryption enabled


### Description

 Checks that your Amazon S3 bucket either has Amazon S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption.

Source
AWS Security Hub
Security Hub control ID: S3.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ElastiCache replication groups of earlier Redis versions should have Redis AUTH enabled


### Description

 Checks if ElastiCache replication groups have Redis AUTH enabled. The check fails for an ElastiCache replication group if the Redis version of its nodes is below 6 and 'AuthToken' is not in use.

Source
AWS Security Hub
Security Hub Control Id: ElastiCache.6

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should require requests to use Secure Socket Layer


### Description

 Checks if S3 buckets have policies that require requests to use Secure Socket Layer (SSL).

Source
AWS Security Hub
Security Hub control ID: S3.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 permissions granted to other AWS accounts in bucket policies should be restricted


### Description

 Checks if the S3 bucket policy allows sensitive bucket-level or object-level actions from a principal in another AWS account. The check fails if any of the following actions are allowed in the S3 bucket policy for a principal in another AWS account: s3:DeleteBucketPolicy, s3:PutBucketAcl, s3:PutBucketPolicy, s3:PutObjectAcl, and s3:PutEncryptionConfiguration.

Source
AWS Security Hub
Security Hub control ID: S3.6

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Auto Scaling Groups


### Description

 Checks for usage that is more than 80% of the Auto Scaling Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Auto Scaling Limits

## RDS Total Storage Quota


### Description

 Checks for usage that is more than 80% of the RDS Total Storage Quota Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon Elasticsearch Service domain error logging to CloudWatch Logs should be enabled


### Description

 Checks whether Amazon Elasticsearch Service domains are configured to send error logs to CloudWatch Logs.

Source
AWS Security Hub
Security Hub control ID: ES.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Classic Load Balancers with SSL/HTTPS listeners should use a certificate provided by AWS Certificate Manager


### Description

 Checks if a Classic Load Balancer uses HTTPS/SSL certificates provided by AWS Certificate Manager. The check fails if a Classic Load Balancer that is configured with an HTTPS/SSL listener does not use a certificate provided by AWS Certificate Manager.

Source
AWS Security Hub
Security Hub control ID: ELB.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Classic Load Balancer listeners should be configured with HTTPS or TLS termination


### Description

 Checks if your Classic Load Balancer listeners are configured with HTTPS or TLS protocol for front-end (client to load balancer) connections. The check is applicable if a Classic Load Balancer has listeners. If your Classic Load Balancer does not have a listener configured, then the check does not report any findings.

Source
AWS Security Hub
Security Hub control ID: ELB.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Relational Database Service (RDS) Reserved Instance Optimization


### Description

 Checks your usage of RDS and provides recommendations on purchase of Reserved Instances to help reduce costs incurred from using RDS On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Instance to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.


### Alert Criteria


Yellow: Optimizing the purchase of RDS Reserved Instances can help reduce costs.


### Recommended Action




See the Cost Explorer page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase RDS Reserved Instances.


### Additional Resources


Information on RDS Reserved Instances and how they can save you money can be found here.
For more information on this recommendation, see Reserved Instance Optimization Check Questions in the Trusted Advisor FAQs.
For more detailed description of fields, see Cost Explorer documentation

## Application load balancer should be configured to drop http headers


### Description

 This check evaluates AWS Application Load Balancers (ALB) to ensure they are configured to drop http headers. By default, ALBs are not configured to drop invalid http header values. This check evaluates all ALBs fails if the attribute value of routing.http.drop_invalid_header_fields.enabled is set to false.

Source
AWS Security Hub
Security Hub control ID: ELB.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Application and Classic Load Balancers logging should be enabled


### Description

 Checks if the Application Load Balancer and the Classic Load Balancer have logging enabled. The check fails if the access_logs.s3.enabled is false.

Source
AWS Security Hub
Security Hub control ID: ELB.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM customer managed policies that you create should not allow wildcard actions for services


### Description

 Checks if the IAM identity-based custom policies have Allow statements that grant permissions for all actions on a service. The check fails if any policy statement includes "Effect": "Allow" with "Action": "Service:".

Source
AWS Security Hub
Security Hub control ID: IAM.21

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS WAF Classic Global Web ACL logging should be enabled


### Description

 Checks if logging is enabled for a WAF global Web ACL. This check fails if logging is not enabled for the Web ACL.

Source
AWS Security Hub
Security Hub control ID: WAF.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Connections to Amazon Elasticsearch Service domains should be encrypted using TLS 1.2


### Description

 Checks whether connections to Amazon Elasticsearch Service domains are required to use TLS 1.2.  The check fails if the Amazon Elasticsearch Service domain TLSSecurityPolicy is not Policy-Min-TLS-1-2-2019-07.

Source
AWS Security Hub
Security Hub control ID: ES.8

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Exposed Access Keys


### Description

 Checks popular code repositories for access keys that have been exposed to the public and for irregular Amazon Elastic Compute Cloud (Amazon EC2) usage that could be the result of a compromised access key. An access key consists of an access key ID and the corresponding secret access key. Exposed access keys pose a security risk to your account and other users, could lead to excessive charges from unauthorized activity or abuse, and violate the AWS Customer Agreement. If your access key is exposed, take immediate action to secure your account. To protect your account from excessive charges, AWS temporarily limits your ability to create certain AWS resources when exposed access keys are identified. This does not make your account secure; it only partially limits the unauthorized usage for which you could be charged. Note: This check does not guarantee the identification of exposed access keys or compromised EC2 instances. You are ultimately responsible for the safety and security of your access keys and AWS resources.   

If a deadline is shown for an access key, AWS may suspend your AWS account if the unauthorized usage is not stopped by that date. If you believe an alert is in error, contact AWS Support.

The information displayed in Trusted Advisor may not reflect the most recent state of your account. No exposed access keys are marked as resolved until all exposed access keys on the account have been resolved. This data synchronization can take up to one week.

### Alert Criteria


Red: Potentially compromised - AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet and may have been compromised (used).
Red: Exposed - AWS has identified an access key ID and corresponding secret access key that have been exposed on the Internet.
Red: Suspected - Irregular Amazon EC2 usage indicates that an access key may have been compromised, but it has not been identified as exposed on the Internet.

### Recommended Action


Delete the affected access key as soon as possible. If the key is associated with an IAM user, see Managing Access Keys for IAM Users.

Check your account for unauthorized usage. Log in to the AWS Management Console and check each service console for suspicious resources. Pay special attention to running Amazon EC2 instances, Spot Instance requests, access keys, and IAM users. You can also check overall usage on the Billing & Cost Management Dashboard.

### Additional Resources


Best Practices for Managing AWS Access Keys
AWS Security Audit Guidelines

## Auto Scaling Group Resources


### Description

 Checks the availability of resources associated with launch configurations and your Auto Scaling groups. Auto Scaling groups that point to unavailable resources cannot launch new Amazon Elastic Compute Cloud (Amazon EC2) instances. When properly configured, Auto Scaling causes the number of Amazon EC2 instances to increase seamlessly during demand spikes and decrease automatically during demand lulls. Auto Scaling groups and launch configurations that point to unavailable resources do not operate as intended.

### Alert Criteria


Red: An Auto Scaling group is associated with a deleted load balancer.
Red: A launch configuration is associated with a deleted Amazon Machine Image (AMI).

### Recommended Action


If the load balancer has been deleted, either create a new load balancer and then create a new Auto Scaling group with the new load balancer, or create a new Auto Scaling group without the load balancer. For information about creating a new Auto Scaling group with a new load balancer, see Set Up an Auto-Scaled and Load-Balanced Application. For information about creating a new Auto Scaling group without a load balancer, see "Create Auto Scaling Group" in Getting Started With Auto Scaling Using the Console.
If the AMI has been deleted, create a new launch configuration using a valid AMI and associate it with an Auto Scaling group. See "Create Launch Configuration" in Getting Started With Auto Scaling Using the Console.

### Additional Resources


Troubleshooting Auto Scaling: Amazon EC2 AMIs
Troubleshooting Auto Scaling: Load Balancer Configuration
Auto Scaling Developer Guide

## Overutilized Amazon EBS Magnetic Volumes


### Description

 Checks for Amazon Elastic Block Store (EBS) Magnetic volumes that are potentially overutilized and might benefit from a more efficient configuration. A Magnetic volume is designed for applications with moderate or bursty I/O requirements, and the IOPS rate is not guaranteed. It delivers approximately 100 IOPS on average, with a best-effort ability to burst to hundreds of IOPS. For consistently higher IOPS, you can use a Provisioned IOPS (SSD) volume. For bursty IOPS, you can use a General Purpose (SSD) volume. For more information, see Amazon EBS Volume Types.

For a list of instance types that support EBS-optimized behavior, see Amazon EBS-Optimized Instances.

To get daily utilization metrics, download the report for this check. The detailed report shows a column for each of the last 14 days. If there is no active EBS volume, the cell is empty. If there is insufficient data to make a reliable measurement, the cell contains "N/A". If there is sufficient data, the cell contains the daily median and the percentage of the variance in relation to the median (for example, "256 / 20%").

### Alert Criteria


Yellow: An Amazon EBS Magnetic volume is attached to an instance that can be EBS-optimized or is part of a cluster compute network with a daily median of more than 95 IOPS, and varies by less than 10% of the median value for at least 7 of the past 14 days.

### Recommended Action


For consistently higher IOPS, you can use a Provisioned IOPS (SSD) volume. For bursty IOPS, you can use a General Purpose (SSD) volume. For more information, see Amazon EBS Volume Types.

### Additional Resources


Amazon Elastic Block Store (Amazon EBS)

## Idle Load Balancers


### Description

 Checks your Elastic Load Balancing configuration for load balancers that are not actively used. Any load balancer that is configured accrues charges. If a load balancer has no associated back-end instances or if network traffic is severely limited, the load balancer is not being used effectively.

### Alert Criteria


Yellow: A load balancer has no active back-end instances.
Yellow: A load balancer has no healthy back-end instances.
Yellow: A load balancer has had less than 100 requests per day for the last 7 days.

### Recommended Action


If your load balancer has no active back-end instances, consider registering instances or deleting your load balancer. See Registering Your Amazon EC2 Instances with Your Load Balancer or Delete Your Load Balancer.
If your load balancer has no healthy back-end instances, see Troubleshooting Elastic Load Balancing: Health Check Configuration.
If your load balancer has had a low request count, consider deleting your load balancer. See Delete Your Load Balancer.

### Additional Resources


Managing Load Balancers
Troubleshoot Elastic Load Balancing

## Neptune DB cluster snapshots should not be public


### Description

 Checks if a Neptune manual DB cluster snapshot is public. The check fails if a Neptune manual DB cluster snapshot is public.

Source
AWS Security Hub
Security Hub Control Id: Neptune.3

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Auto scaling groups associated with a load balancer should use load balancer health checks


### Description

 Checks if your Auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks.

Source
AWS Security Hub
Security Hub control ID: AutoScaling.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Neptune DB clusters should have deletion protection enabled


### Description

 Checks if a Neptune DB cluster has deletion protection enabled. The check fails if a Neptune DB cluster doesn't have deletion protection enabled.

Source
AWS Security Hub
Security Hub Control Id: Neptune.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Security groups should only allow unrestricted incoming traffic for authorized ports


### Description

 Checks if the security groups allow unrestricted incoming traffic. The check fails if ports allow unrestricted traffic on ports other than 80 and 443, which are default values for parameter authorizedTcpPorts.

Source
AWS Security Hub
Security Hub control ID: EC2.18

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon S3 Bucket Logging


### Description

 Checks the logging configuration of Amazon Simple Storage Service (Amazon S3) buckets. When server access logging is enabled, detailed access logs are delivered hourly to a bucket that you choose. An access log record contains details about each request, such as the request type, the resources specified in the request, and the time and date the request was processed. By default, bucket logging is not enabled; you should enable logging if you want to perform security audits or learn more about users and usage patterns.

When logging is initially enabled, the configuration is automatically validated; however, future modifications can result in logging failures. This check examines explicit Amazon S3 bucket permissions, but it does not examine associated bucket policies that might override the bucket permissions.

### Alert Criteria


Yellow: The bucket does not have server access logging enabled.
Yellow: The target bucket permissions do not include the root account, so Trusted Advisor cannot check it.
Red: The target bucket does not exist.
Red: The target bucket and the source bucket have different owners.
Red: The log deliverer does not have write permissions for the target bucket.

### Recommended Action


Enable bucket logging for most buckets. See Enabling Logging Using the Console and Enabling Logging Programmatically. 
If the target bucket permissions do not include the root account and you want Trusted Advisor to check the logging status, add the root account as a grantee. See Editing Bucket Permissions.
If the target bucket does not exist, select an existing bucket as a target or create a new one and select it. See Managing Bucket Logging.
If the target and source have different owners, change the target bucket to one that has the same owner as the source bucket. See Managing Bucket Logging.
If the log deliverer does not have write permissions for the target (Write not enabled), grant Upload/Delete permissions to the Log Delivery group. See Editing Bucket Permissions.


### Additional Resources


Working with Buckets
Server Access Logging
Server Access Log Format
Deleting Log Files

## SNS topics should be encrypted at-rest using AWS KMS


### Description

 Checks if an Amazon SNS topic is encrypted at rest using AWS KMS.

Source
AWS Security Hub
Security Hub control ID: SNS.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ELB Cross-Zone Load Balancing


### Description

 With Cross-zone load balancing turned off, there is a risk of service unavailability due to uneven distribution of traffic or backend overloading. This problem can occur when clients incorrectly cache DNS information, or when there are an unequal number of instances in each Availability Zone (for example, if you have taken down some instances for maintenance).

### Alert Criteria


Yellow: Cross-zone load balancing is not enabled for a load balancer.

### Recommended Action


Confirm that the Amazon EC2 instances registered with the load balancer are launched in multiple Availability Zones, and then enable cross-zone load balancing for the load balancer. For more information, see Availability Zones and Regions and Enable or Disable Cross-Zone Load Balancing for Your Load Balancer.

### Additional Resources


Request Routing
Elastic Load Balancing Concepts

## CloudFormation Stacks


### Description

 Checks for usage that is more than 80% of the CloudFormation Stacks Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


CloudFormation Limits

## EBS Provisioned IOPS SSD (io2) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS Provisioned IOPS SSD (io2) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## EC2 Auto Scaling groups should use EC2 launch templates


### Description

 Checks if an Amazon EC2 Auto Scaling group is created from an EC2 launch template. This check fails if an Amazon EC2 Auto Scaling group is not created with a launch template or if a launch template is not specified in a mixed instances policy.

Source
AWS Security Hub
Security Hub Control Id: AutoScaling.9

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway routes should specify an authorization type


### Description

 Checks if Amazon API Gateway routes have an authorization type. The check fails if the API Gateway route does not specify an authorization type

Source
AWS Security Hub
Security Hub Control Id: APIGateway.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Elasticsearch domains should encrypt data sent between nodes


### Description

 Checks if Elasticsearch domains have node-to-node encryption enabled.

Source
AWS Security Hub
Security Hub control ID: ES.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Users should not have root access to SageMaker notebook instances


### Description

 Checks if root access is turned off for Amazon SageMaker notebook instances. The check fails if root access is turned on for a SageMaker notebook instance.

Source
AWS Security Hub
Security Hub Control Id: SageMaker.3

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## An RDS event notifications subscription should be configured for critical database parameter group events


### Description

 Checks if an Amazon RDS Event subscription for RDS parameter groups is configured to notify on event category of "configuration change".

Source
AWS Security Hub
Security Hub control ID: RDS.21

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Security contact information should be provided for an AWS account.


### Description

 Checks if an Amazon Web Services (AWS) account has security contact information. The check fails if security contact information is not provided for the account.

Source
AWS Security Hub
Security Hub Control Id: Account.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## An RDS event notifications subscription should be configured for critical database instance events


### Description

 Checks if an Amazon RDS Event subscription for RDS instances is configured to notify on event categories of both "maintenance", "configuration change", and "failure".

Source
AWS Security Hub
Security Hub control ID: RDS.20

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ELB Application Load Balancers


### Description

 Checks for usage that is more than 80% of the ELB Application Load Balancers Limit. Classic Load Balancers and Network Load Balancers have separate limits. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


AWS Service Limits - Elastic Load Balancing default service limits

## IAM Server Certificates


### Description

 Checks for usage that is more than 80% of the IAM Server Certificates Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## SageMaker notebook instances should be launched in a custom VPC


### Description

 Checks if an Amazon SageMaker notebook instance is launched within a custom VPC. The check fails if a SageMaker notebook instance is not launched within a custom VPC.

Source
AWS Security Hub
Security Hub Control Id: SageMaker.2

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS instances should not use a database engine default port


### Description

 Checks if RDS instances use the default port of that database engine.

Source
AWS Security Hub
Security Hub control ID: RDS.23

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should not point to non-existent S3 origins


### Description

 Checks if Amazon CloudFront distributions are pointing to non-existent S3 origins. The check fails for a CloudFront distribution if the origin is configured to point to a non-existent bucket. This check only applies to CloudFront distributions where an S3 bucket without static website hosting is the S3 origin.

Source
AWS Security Hub
Security Hub Control Id: CloudFront.12

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## An RDS event notifications subscription should be configured for critical database security group events


### Description

 Checks if an Amazon RDS Event subscription for RDS security groups is configured to notify on event categories of both "configuration change" and "failure".

Source
AWS Security Hub
Security Hub control ID: RDS.22

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront Header Forwarding and Cache Hit Ratio


### Description

 Checks the HTTP request headers that CloudFront currently receives from the client and forwards to your origin server. Some headers, such as Date or User-Agent, significantly reduce the cache hit ratio (the proportion of requests that are served from a CloudFront edge cache). This increases the load on your origin and reduces performance because CloudFront must forward more requests to your origin.

### Alert Criteria


Yellow: One or more request headers that CloudFront forwards to your origin might significantly reduce your cache hit ratio.

### Recommended Action


Consider whether the request headers provide enough benefit to justify the negative effect on the cache hit ratio. If your origin returns the same object regardless of the value of a given header, we recommend that you don't configure CloudFront to forward that header to the origin. For more information, see Configuring CloudFront to Cache Objects Based on Request Headers.

### Additional Resources


Increasing the Proportion of Requests that Are Served from CloudFront Edge Caches
CloudFront Cache Statistics Reports
HTTP Request Headers and CloudFront Behavior

## A WAF Regional rule group should have at least one rule


### Description

 Checks if a WAF Regional rule group has at least one rule. The check fails if no rules are present within a rule group.

Source
AWS Security Hub
Security Hub Control Id: WAF.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Unused IAM user credentials should be removed


### Description

 Checks if your IAM users have passwords or active access keys that were not used within the previous 90 days.

Source
AWS Security Hub
Security Hub control ID: IAM.8

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Load Balancer Optimization


### Description

 Checks your load balancer configuration. To help increase the level of fault tolerance in Amazon Elastic Compute Cloud (EC2) when using Elastic Load Balancing, we recommend running an equal number of instances across multiple Availability Zones in a region. A load balancer that is configured accrues charges, so this is a cost-optimization check as well.

### Alert Criteria


Yellow: A load balancer is enabled for a single Availability Zone.
Yellow: A load balancer is enabled for an Availability Zone that has no active instances.
Yellow: The Amazon EC2 instances that are registered with a load balancer are unevenly distributed across Availability Zones. (The difference between the highest and lowest instance counts in utilized Availability Zones is more than 1, and the difference is more than 20% of the highest count.)

### Recommended Action


Ensure that your load balancer points to active and healthy instances in at least two Availability Zones. For more information, see Add Availability Zone.
If your load balancer is configured for an Availability Zone with no healthy instances, or if there is an imbalance of instances across the Availability Zones, determine if all the Availability Zones are necessary. Omit any unnecessary Availability Zones and ensure there is a balanced distribution of instances across the remaining Availability Zones. For more information, see Remove Availability Zone.

### Additional Resources


Availability Zones and Regions
Managing Load Balancers
Best Practices in Evaluating Elastic Load Balancing

## EBS Provisioned IOPS SSD (io1) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS Provisioned IOPS SSD (io1) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## A WAF Regional web ACL should have at least one rule or rule group


### Description

 Checks if a WAF Regional web ACL contains any WAF rules or WAF rule groups. This check fails if a web ACL does not contain any WAF rules or rule groups.

Source
AWS Security Hub
Security Hub Control Id: WAF.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECS task definitions should have secure networking modes and user definitions.


### Description

 Checks if an Amazon ECS Task Definition with host networking mode has "privileged" or "user" container definitions. The check fails with host network mode and container definitions are privileged=false or empty and user=root or empty.

Source
AWS Security Hub
Security Hub control ID: ECS.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon RDS Idle DB Instances


### Description

 Checks the configuration of your Amazon Relational Database Service (Amazon RDS) for any DB instances that appear to be idle. If a DB instance has not had a connection for a prolonged period of time, you can delete the instance to reduce costs. If persistent storage is needed for data on the instance, you can use lower-cost options such as taking and retaining a DB snapshot. Manually created DB snapshots are retained until you delete them.
 
 
### Alert Criteria


 
Yellow: An active DB instance has not had a connection in the last 7 days.
 
 
### Recommended Action


 
Consider taking a snapshot of the idle DB instance and then either stopping it or deleting it. Stopping the DB instance removes some of the costs for it, but does not remove storage costs. A stopped instance keeps all automated backups based upon the configured retention period. Stopping a DB instance usually incurs additional costs when compared to deleting the instance and then retaining only the final snapshot. See Stopping an Amazon RDS DB Instance Temporarily and Deleting a DB Instance with a Final Snapshot.
 
 
### Additional Resources


 
Back Up and Restore

## A WAF global rule should have at least one condition


### Description

 Checks if a WAF global rule has at least one condition. This check fails if no conditions are present within a rule.

Source
AWS Security Hub
Security Hub Control Id: WAF.6

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ECS services should not have public IP addresses assigned to them automatically


### Description

 Checks if ECS services are configured to automatically assign public IP addresses. This check fails if AssignPublicIP is ENABLED.

Source
AWS Security Hub
Security Hub control ID: ECS.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Large Number of EC2 Security Group Rules Applied to an Instance


### Description

 Checks for Amazon Elastic Compute Cloud (EC2) instances that have a large number of security group rules. Performance can be degraded if an instance has a large number of rules.

### Alert Criteria


Yellow: An Amazon EC2-VPC instance has more than 50 security group rules.
Yellow: An Amazon EC2-Classic instance has more than 100 security group rules.

### Recommended Action


Reduce the number of rules associated with an instance by deleting unnecessary or overlapping rules. For more information, see Deleting Rules from a Security Group.

### Additional Resources


Amazon EC2 Security Groups

## A WAF global rule group should have at least one rule


### Description

 Checks if a WAF global rule group has at least one rule. The check fails if no rules are present within a rule group.

Source
AWS Security Hub
Security Hub Control Id: WAF.7

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Elasticsearch Service domains should be in a VPC


### Description

 Checks whether Amazon Elasticsearch Service domains are in a VPC. It does not evaluate the VPC subnet routing configuration to determine public reachability. This check also does not check whether the Amazon OpenSearch Service resource-based policy permits public access by other accounts or external entities. You should ensure that Amazon Elasticsearch Service domains are not attached to public subnets. See Resource-based policies (https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html#ac-types-resource) in the Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) Developer Guide. You should also ensure that your VPC is configured according to the recommended best practices. See Security best practices for your VPC (https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) in the Amazon VPC User Guide.

Source
AWS Security Hub
Security Hub control ID: ES.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## A WAF global web ACL should have at least one rule or rule group


### Description

 Checks if a WAF global web ACL contains any WAF rules or WAF rule groups. This check fails if a web ACL does not contain any WAF rules or WAF rule groups.

Source
AWS Security Hub
Security Hub Control Id: WAF.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Elastic Beanstalk environments should have enhanced health reporting enabled


### Description

 Checks if enhanced health reporting is enabled for your AWS Elastic Beanstalk environments.

Source
AWS Security Hub
Security Hub control ID: ElasticBeanstalk.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Redshift Reserved Node Optimization


### Description

 Checks your usage of Redshift and provides recommendations on purchase of Reserved Nodes to help reduce costs incurred from using Redshift On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Nodes to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.

### Alert Criteria


Yellow: Optimizing the purchase of Redshift Reserved Nodes can help reduce costs.

### Recommended Action


See the Cost Explorer page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase Redshift Reserved Nodes.

### Additional Resources


Information on Redshift Reserved Nodes and how they can save you money can be found here.
For more information on this recommendation, see Reserved Instance Optimization Check Questions in the Trusted Advisor FAQs.
For more detailed description of fields, see Cost Explorer documentation

## Elastic Beanstalk managed platform updates should be enabled


### Description

 Checks if managed platform updates are enabled for the AWS Elastic Beanstalk environment.

Source
AWS Security Hub
Security Hub control ID: ElasticBeanstalk.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Route 53 Deleted Health Checks


### Description

 Checks for resource record sets that are associated with health checks that have been deleted. Amazon Route 53 does not prevent you from deleting a health check that is associated with one or more resource record sets. If you delete a health check without updating the associated resource record sets, the routing of DNS queries for your DNS failover configuration will not work as intended. Hosted zones created by AWS services won’t appear in your check results.


### Alert Criteria


Yellow: A resource record set is associated with a health check that has been deleted.

### Recommended Action


Create a new health check and associate it with the resource record set; see Creating, Updating, and Deleting Health Checks and Adding Health Checks to Resource Record Sets.


Additional Information
Amazon Route 53 Health Checks and DNS Failover
How Health Checks Work in Simple Amazon Route 53 Configurations

## Application, Network and Gateway Load Balancers should span multiple Availability Zones


### Description

 Checks if an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) has registered instances from multiple Availability Zones. The check fails if an Elastic Load Balancer V2 has instances registered in less than 2 Availability Zones.

Source
AWS Security Hub
Security Hub Control Id: ELB.13

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront Content Delivery Optimization


### Description

 Checks for cases where data transfer from Amazon Simple Storage Service (Amazon S3) buckets could be accelerated by using Amazon CloudFront, the AWS global content delivery service. When you configure CloudFront to deliver your content, requests for your content are automatically routed to the nearest edge location where content is cached, so it can be delivered to your users with the best possible performance. A high ratio of data transferred out to the data stored in the bucket indicates that you could benefit from using Amazon CloudFront to deliver the data. 

To estimate the retrieval activity of users, only data transferred by using a GET request is counted for this check. In addition, the transfer activity from the last 24 hours is not included. 


### Alert Criteria


Yellow: The amount of data transferred out of the bucket to your users by GET requests in the 30 days preceding the check is at least 25 times greater than the average amount of data stored in the bucket.
Red: The amount of data transferred out of the bucket to your users by GET requests in the 30 days preceding the check is at least 10 TB and at least 25 times greater than the average amount of data stored in the bucket.


### Recommended Action


Consider using CloudFront for better performance; see Amazon CloudFront Product Details. 

If the data transferred is 10 TB per month or more, see Amazon CloudFront Pricing to explore possible cost savings.


### Additional Resources


Amazon CloudFront Developer Guide
AWS Case Study: PBS

## OpenSearch domains should have at least three data nodes.


### Description

 Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and "zoneAwarenessEnabled" is true.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.6

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM authentication should be configured for RDS instances


### Description

 Checks if an RDS DB instance has IAM database authentication enabled.

Source
AWS Security Hub
Security Hub control ID: RDS.10

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RSA certificates managed by ACM should use a key length of at least 2,048 bits


### Description

 Checks if RSA certificates managed by AWS Certificate Manager use a key length of at least 2,048 bits. The check fails if the key length is smaller than 2,048 bits.

Source
AWS Security Hub
Security Hub Control Id: ACM.2

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM authentication should be configured for RDS clusters


### Description

 Checks if an RDS DB cluster has IAM database authentication enabled.

Source
AWS Security Hub
Security Hub control ID: RDS.12

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS AppSync should have request-level and field-level logging turned on


### Description

 Checks if an AWS AppSync API has request-level and field-level logging turned on. The check fails if request-level logging isn't turned on or if the field resolver log level is set to ‘None’.

Source
AWS Security Hub
Security Hub Control Id: AppSync.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS automatic minor version upgrades should be enabled


### Description

 Checks if automatic minor version upgrades are enabled for the Amazon RDS database instance.

Source
AWS Security Hub
Security Hub control ID: RDS.13

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should use origin access control


### Description

 Checks if an Amazon CloudFront distribution with an Amazon S3 origin has origin access check (OAC) configured. The check fails if OAC isn't configured.

Source
AWS Security Hub
Security Hub Control Id: CloudFront.13

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB clusters should be configured to copy tags to snapshots


### Description

 Checks if RDS DB clusters are configured to copy all tags to snapshots when the snapshots are created.

Source
AWS Security Hub
Security Hub control ID: RDS.16

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EKS cluster endpoints should not be publicly accessible


### Description

 Checks if an Amazon EKS cluster endpoint is publicly accessible. The check fails if an EKS cluster has an endpoint that is publicly accessible.

Source
AWS Security Hub
Security Hub Control Id: EKS.1

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB instances should be configured to copy tags to snapshots


### Description

 Checks if RDS DB instances are configured to copy all tags to snapshots when the snapshots are created.

Source
AWS Security Hub
Security Hub control ID: RDS.17

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ElastiCache for Redis cache clusters should have auto minor version upgrades enabled


### Description

 This check evaluates if auto minor version upgrades are enabled for ElastiCache for Redis cache clusters. This check fails if the ElastiCache for Redis cache cluster does not have auto minor version upgrades enabled.

Source
AWS Security Hub
Security Hub Control Id: ElastiCache.2

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS instances should be deployed in a VPC


### Description

 Checks if an RDS instance is deployed in a VPC (EC2-VPC).

Source
AWS Security Hub
Security Hub control ID: RDS.18

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS Event Subscriptions


### Description

 Checks for usage that is more than 80% of the RDS Event Subscriptions Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## DynamoDB Write Capacity


### Description

 Checks for usage that is more than 80% of the DynamoDB Provisioned Throughput Limit for Writes per Account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


DynamoDB Limits

## A WAFV2 web ACL should have at least one rule or rule group


### Description

 Checks if a WAFV2 web ACL contains at least one WAF rule or WAF rule group. The check fails if a web ACL does not contain any WAF rule or rule group.

Source
AWS Security Hub
Security Hub Control Id: WAF.10

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances should be managed by AWS Systems Manager


### Description

 Checks if the Amazon EC2 instances in your account are managed by AWS Systems Manager.

Source
AWS Security Hub
Security Hub control ID: SSM.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Comprehend Endpoint Access Risk


### Description

 Checks the AWS Key Management Service (AWS KMS) key permissions for an endpoint where the underlying model was encrypted by using customer managed keys. If the customer managed key is disabled or the key policy was changed to alter the allowed permissions for Amazon Comprehend, the endpoint availability might be affected.
Note: This check is automatically refreshed multiple times a day. It might take a few hours for the latest results to appear.

### Alert Criteria


Red: The customer managed key is disabled or the key policy was changed to alter the allowed permissions for Amazon Comprehend access.

### Recommended Action


If the customer managed key was disabled, we recommend that you enable it. For more information, see Enabling keys. If the key policy was altered and you want to keep using the endpoint, we recommend that you update the KMS key policy. For more information, see Changing a key policy.

### Additional Resources


KMS Key Encryption Permissions


## EC2 launch templates should not assign public IPs to network interfaces


### Description

 Checks if Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces upon launch. The check fails if an EC2 launch template is configured to assign a public IP address to network interfaces or if there is at least one network interface that has a public IP address.

Source
AWS Security Hub
Security Hub Control Id: EC2.25

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances managed by Systems Manager should have a patch compliance status of COMPLIANT after a patch installation


### Description

 Checks if the compliance status of the Amazon EC2 Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance. It only assesses instances that are managed by AWS Systems Manager Patch Manager.

Source
AWS Security Hub
Security Hub control ID: SSM.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## High Utilization Amazon EC2 Instances


### Description

 Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days and alerts you if the daily CPU utilization was more than 90% on 4 or more days. Consistent high utilization can indicate optimized, steady performance, but it can also indicate that an application does not have enough resources. To get daily CPU utilization data, download the report for this check.

### Alert Criteria


Yellow: An instance had more than 90% daily average CPU utilization on at least 4 of the previous 14 days.

### Recommended Action


Consider adding more instances. For information about scaling the number of instances based on demand, see What is Auto Scaling?

### Additional Resources


Monitoring Amazon EC2
Instance Metadata and User Data
Amazon CloudWatch Developer Guide
Auto Scaling Developer Guide

## Access logging should be configured for API Gateway V2 Stages


### Description

 Checks if Amazon API Gateway V2 stages have access logging configured. This check fails if access log settings aren’t defined.

Source
AWS Security Hub
Security Hub Control Id: APIGateway.9

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances managed by Systems Manager should have an association compliance status of COMPLIANT


### Description

 Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association is executed on an instance.

Source
AWS Security Hub
Security Hub control ID: SSM.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Kinesis Shards per Region


### Description

 Checks for usage that is more than 80% of the Kinesis Shards per Region Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Kinesis Streams Limits

## Amazon EC2 Auto Scaling group should cover multiple Availability Zones


### Description

 Checks if an Auto Scaling group spans multiple Availability Zones. The check fails if an Auto Scaling group does not span multiple availability zones.

Source
AWS Security Hub
Security Hub Control Id: AutoScaling.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## SSM documents should not be public


### Description

 Checks if AWS Systems Manager documents that the account owns are public. This check fails if SSM documents that have "Self" as the owner are public.

Source
AWS Security Hub
Security Hub control ID: SSM.4

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Comprehend Underutilized Endpoints


### Description

 Checks the throughput configuration of your endpoints. This check alerts you when endpoints are not actively used for real-time inference requests. An endpoint that isn’t used for more than 15 consecutive days is considered underutilized. All endpoints accrue charges based on both the throughput set and the length of time that the endpoint is active.
Note: This check is automatically refreshed once a day.

### Alert Criteria


Yellow: The endpoint is active, but hasn’t been used for real-time inference requests in the past 15 days.

### Recommended Action


If the endpoint hasn’t been used in the past 15 days, we recommend that you define a scaling policy for the resource by using Application Autoscaling.
If the endpoint has a scaling policy defined and hasn’t been used in the past 30 days, consider deleting the endpoint and using asynchronous inference. For more information, see Deleting an endpoint with Amazon Comprehend.


## Elastic File System should be configured to encrypt file data at-rest using AWS KMS


### Description

 Checks if Amazon Elastic File System (Amazon EFS) is configured to encrypt the file data using AWS Key Management Service (AWS KMS). The check will fail if the encrypted key is set to false on DescribeFileSystems or if the KmsKeyId key on DescribeFileSystems does not match the KmsKeyId parameter.

Source
AWS Security Hub
Security Hub control ID: EFS.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM Instance Profiles


### Description

 Checks for usage that is more than 80% of the IAM Instance Profiles Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## Route 53 Hosted Zones


### Description

 Checks for usage that is more than 80% of the Route 53 Hosted Zones Limit per account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Route 53 Limits

## Amazon EBS Provisioned IOPS (SSD) Volume Attachment Configuration


### Description

 Checks for Provisioned IOPS (SSD) volumes that are attached to an Amazon EBS-optimizable Amazon Elastic Compute Cloud (Amazon EC2) instance that is not EBS-optimized. Provisioned IOPS (SSD) volumes in the Amazon Elastic Block Store (Amazon EBS) are designed to deliver the expected performance only when they are attached to an EBS-optimized instance.

### Alert Criteria


Yellow: An Amazon EC2 instance that can be EBS-optimized has an attached Provisioned IOPS (SSD) volume but the instance is not EBS-optimized.

### Recommended Action


Create a new instance that is EBS-optimized, detach the volume, and reattach the volume to your new instance. For more information, see Amazon EBS-Optimized Instances and Attaching an Amazon EBS Volume to an Instance.

### Additional Resources


Amazon EBS Volume Types
Amazon EBS Volume Performance

## ECS clusters should use Container Insights


### Description

 Checks if ECS clusters use Container Insights. This check fails if Container Insights are not set up for a cluster.

Source
AWS Security Hub
Security Hub Control Id: ECS.12

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EFS access points should enforce a root directory


### Description

 Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a root directory. This check fails if the value of 'Path' is set to '/' (default root directory of the file system).

Source
AWS Security Hub
Security Hub Control Id: EFS.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Lambda functions should use supported runtimes


### Description

 Checks that the lambda function settings for runtimes, match the expected values set for the supported runtimes for each language. The supported runtimes this check assesses for are: nodejs18.x, nodejs16.x, nodejs14.x, nodejs12.x, python3.10, python3.9, python3.8, python3.7, java11, java8, java8.al2, go1.x, dotnet6, ruby2.7.

Source
AWS Security Hub
Security Hub control ID: Lambda.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EFS access points should enforce a user identity


### Description

 Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity. This check fails if ‘PosixUser’ is not defined under ‘configuration’ or if parameters are provided and there is no match in the corresponding parameter.

Source
AWS Security Hub
Security Hub Control Id: EFS.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Lambda function policies should prohibit public access


### Description

 Checks if the AWS Lambda function policy attached to the Lambda resource prohibits public access. If the Lambda function policy allows public access, the check fails.

Source
AWS Security Hub
Security Hub control ID: Lambda.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EKS clusters should run on a supported Kubernetes version


### Description

 Checks if an EKS cluster is running on a supported Kubernetes version. The check fails if the EKS cluster is running on an unsupported version.

Source
AWS Security Hub
Security Hub Control Id: EKS.2

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Database Migration Service replication instances should not be public


### Description

 Checks if AWS Database Migration Service replication instances are public by examining the PubliclyAccessible field value.

Source
AWS Security Hub
Security Hub control ID: DMS.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2-VPC Elastic IP Address


### Description

 Checks for usage that is more than 80% of the EC2-VPC Elastic IP Address Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


VPC Elastic IP Limits

## Unassociated Elastic IP Addresses


### Description

 Checks for Elastic IP addresses (EIPs) that are not associated with a running Amazon Elastic Compute Cloud (Amazon EC2) instance. EIPs are static IP addresses designed for dynamic cloud computing. Unlike traditional static IP addresses, EIPs can mask the failure of an instance or Availability Zone by remapping a public IP address to another instance in your account. A nominal charge is imposed for an EIP that is not associated with a running instance.

### Alert Criteria


Yellow: An allocated Elastic IP address (EIP) is not associated with a running Amazon EC2 instance.

### Recommended Action


Associate the EIP with a running active instance, or release the unassociated EIP. For more information, see Associating an Elastic IP Address with a Different Running Instance and Releasing an Elastic IP Address.

### Additional Resources


Elastic IP Addresses

## RDS Max Auths per Security Group


### Description

 Checks for usage that is more than 80% of the RDS Max Auths per Security Group Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon EBS Snapshots


### Description

 Checks the age of the snapshots for your Amazon Elastic Block Store (Amazon EBS) volumes (available or in-use). Even though Amazon EBS volumes are replicated, failures can occur. Snapshots are persisted to Amazon Simple Storage Service (Amazon S3) for durable storage and point-in-time recovery.

### Alert Criteria


Yellow: The most recent volume snapshot is between 7 and 30 days old.
Red: The most recent volume snapshot is more than 30 days old.
Red: The volume does not have a snapshot.

### Recommended Action


Create weekly or monthly snapshots of your volumes. For more information, see Creating an Amazon EBS Snapshot.

### Additional Resources


Amazon Elastic Block Store (Amazon EBS)

## Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)


### Description

 Checks if only IMDSv2 is enabled. This check fails if the metadata version is not included in the launch configuration or if both IMDSv1 and IMDSv2 are enabled.

Source
AWS Security Hub
Security Hub Control Id: AutoScaling.3

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## VPC flow logging should be enabled in all VPCs


### Description

 Checks if Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPCs. The traffic type is set to 'Reject'.

Source
AWS Security Hub
Security Hub control ID: EC2.6

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon OpenSearch Service Reserved Instance Optimization


### Description

 Checks your usage of Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) and provides recommendations on purchase of Reserved Instances to help reduce costs incurred from using Amazon OpenSearch Service On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Instance to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.

### Alert Criteria


Yellow: Optimizing the purchase of Amazon OpenSearch Service Reserved Instances can help reduce costs.

### Recommended Action


See the Cost Explorer page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase Amazon OpenSearch Service Reserved Instances.

### Additional Resources


Information on Amazon OpenSearch Service Reserved Instances and how they can save you money can be found here.
For more information on this recommendation, see Reserved Instance Optimization Check Questions in the Trusted Advisor FAQs.
For more detailed description of fields, see Cost Explorer documentation

## Auto Scaling group launch configuration should not have a metadata response hop limit greater than 1


### Description

 Checks the number of network hops that the metadata token can travel. This check fails if the metadata response hop limit is greater than 1.

Source
AWS Security Hub
Security Hub Control Id: AutoScaling.4

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances should not have a public IPv4 address


### Description

 Checks if EC2 instances have a public IP address. The check fails if the publicIp field is present in the EC2 instance configuration item. This check applies to IPv4 addresses only.

Source
AWS Security Hub
Security Hub control ID: EC2.9

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS Clusters


### Description

 Checks for usage that is more than 80% of the RDS Clusters Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## CloudFormation stacks should be integrated with Simple Notification Service (SNS)


### Description

 Checks if your CloudFormation stacks are sending event notifications to SNS topic. This check fails if CloudFormation stacks are not sending event notifications to an SNS topic.

Source
AWS Security Hub
Security Hub Control Id: CloudFormation.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances should use Instance Metadata Service Version 2 (IMDSv2)


### Description

 Checks if your Amazon Elastic Compute Cloud (Amazon EC2) instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2). The check passes if HttpTokens is set to required for IMDSv2. The check fails if HttpTokens is set to optional.

Source
AWS Security Hub
Security Hub control ID: EC2.8

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should not use deprecated SSL protocols between edge locations and custom origins


### Description

 Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and your custom origins. This check fails for a CloudFront distribution if it has a 'CustomOriginConfig' where ‘OriginSslProtocols’ includes ‘SSLv3’.

Source
AWS Security Hub
Security Hub Control Id: CloudFront.10

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway should be associated with a WAF Web ACL


### Description

 Checks to see if an API Gateway stage is using an AWS WAF Web ACL. This check fails if an AWS WAF Web ACL is not attached to a REST API Gateway stage.

Source
AWS Security Hub
Security Hub control ID: APIGateway.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Low Utilization Amazon EC2 Instances


### Description

 Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days and alerts you if the daily CPU utilization was 10% or less and network I/O was 5 MB or less on 4 or more days. Running instances generate hourly usage charges. Although some scenarios can result in low utilization by design, you can often lower your costs by managing the number and size of your instances.

Estimated monthly savings are calculated by using the current usage rate for On-Demand Instances and the estimated number of days the instance might be underutilized. Actual savings will vary if you are using Reserved Instances or Spot Instances, or if the instance is not running for a full day. To get daily utilization data, download the report for this check. 


### Alert Criteria


Yellow: An instance had 10% or less daily average CPU utilization and 5 MB or less network I/O on at least 4 of the previous 14 days.

### Recommended Action


Consider stopping or terminating instances that have low utilization, or scale the number of instances by using Auto Scaling. For more information, see Stop and Start Your Instance, Terminate Your Instance, and What is Auto Scaling?

### Additional Resources


Monitoring Amazon EC2
Instance Metadata and User Data
Amazon CloudWatch Developer Guide
Auto Scaling Developer Guide

## EC2 Transit Gateways should not automatically accept VPC attachment requests


### Description

 Checks if EC2 Transit Gateways are automatically accepting shared VPC attachments requests. This check will fail for a Transit Gateway that automatically accept shared VPC attachment requests.

Source
AWS Security Hub
Security Hub Control Id: EC2.23

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## DynamoDB Accelerator (DAX) clusters should be encrypted at rest


### Description

 Checks if a DAX cluster is encrypted at rest.

Source
AWS Security Hub
Security Hub control ID: DynamoDB.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 paravirtual instance types should not be used


### Description

 Checks if the virtualization type of an EC2 instance is paravirtual. The check fails for an EC2 instance if ‘virtualizationType’ is set to ‘paravirtual’.

Source
AWS Security Hub
Security Hub Control Id: EC2.24

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway REST and WebSocket API execution logging should be enabled


### Description

 Checks if all stages of Amazon API Gateway REST and WebSocket APIs have logging enabled. The check fails if logging is not enabled for all methods of a stage or if loggingLevel is neither ERROR nor INFO.

Source
AWS Security Hub
Security Hub control ID: APIGateway.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ECS Fargate services should run on the latest Fargate platform version


### Description

 Checks if ECS Fargate services is running the latest Fargate platform version. This check fails if the platform version is not latest.

Source
AWS Security Hub
Security Hub Control Id: ECS.10

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway REST API stages should be configured to use SSL certificates for backend authentication


### Description

 Checks if Amazon API Gateway REST API stages have SSL certificates configured that backend systems can use to authenticate that incoming requests are from the API Gateway.

Source
AWS Security Hub
Security Hub control ID: APIGateway.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway REST API stages should have AWS X-Ray tracing enabled


### Description

 Checks if AWS X-Ray active tracing is enabled for your Amazon API Gateway REST API stages.

Source
AWS Security Hub
Security Hub control ID: APIGateway.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Underutilized Amazon Redshift Clusters


### Description

 Checks your Amazon Redshift configuration for clusters that appear to be underutilized. If an Amazon Redshift cluster has not had a connection for a prolonged period of time or is using a low amount of CPU, you can use lower-cost options such as downsizing the cluster or shutting down the cluster and taking a final snapshot. Final snapshots are retained even after you delete your cluster.

### Alert Criteria


Yellow: A running cluster has not had a connection in the last 7 days.
Yellow: A running cluster had less than 5% cluster-wide average CPU utilization for 99% of the last 7 days.

### Recommended Action


Consider shutting down the cluster and taking a final snapshot, or downsizing the cluster. See Shutting Down and Deleting Clusters and Resizing a Cluster.

### Additional Resources


Amazon CloudWatch Developer Guide

## Amazon ElastiCache Reserved Node Optimization


### Description

 Checks your usage of ElastiCache and provides recommendations on purchase of Reserved Nodes to help reduce costs incurred from using ElastiCache On-Demand. AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of Reserved Node to purchase to maximize your savings. This check covers recommendations based on partial upfront payment option with 1-year or 3-year commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.

### Alert Criteria


Yellow: Optimizing the purchase of ElastiCache Reserved Nodes can help reduce costs.

### Recommended Action


See the Cost Explorer page for more detailed recommendations, customization options (e.g. look-back period, payment option, etc.) and to purchase ElastiCache Reserved Nodes.

### Additional Resources


Information on ElastiCache Reserved Nodes and how they can save you money can be found here.
For more information on this recommendation, see Reserved Instance Optimization Check Questions in the Trusted Advisor FAQs.
For more detailed description of fields, see Cost Explorer documentation

## OpenSearch domains should have fine-grained access control enabled


### Description

 Checks if Amazon OpenSearch domains have fine-grained access check enabled. This check fails if the fine-grained access check is not enabled.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.7

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Redshift clusters should not use the default database name


### Description

 Checks if a Redshift cluster has changed the database name from its default value. This check will fail if the database name for a Redshift cluster is set to “dev”

Source
AWS Security Hub
Security Hub Control Id: Redshift.9

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM root user access key should not exist


### Description

 Checks if the root user access key is available.

Source
AWS Security Hub
Security Hub control ID: IAM.4

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should have lifecycle policies configured


### Description

 Checks if a lifecycle policy is configured for an S3 bucket. This check fails if the lifecycle policy is not configured for an S3 bucket.

Source
AWS Security Hub
Security Hub Control Id: S3.13

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## MFA should be enabled for all IAM users that have a console password


### Description

 Checks if AWS Multi-Factor Authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that use a console password.

Source
AWS Security Hub
Security Hub control ID: IAM.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Logging of delivery status should be enabled for notification messages sent to a topic


### Description

 Checks if logging is enabled for the delivery status of notification messages sent to a topic for the endpoints. This check fails if the delivery status notification for messages is not enabled.

Source
AWS Security Hub
Security Hub Control Id: SNS.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Hardware MFA should be enabled for the root user


### Description

 Checks if your AWS account is enabled to use hardware multi-factor authentication (MFA) device to sign in with root credentials.

Source
AWS Security Hub
Security Hub control ID: IAM.6

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## A WAF Regional rule should have at least one condition


### Description

 Checks if a WAF Regional rule has at least one condition. The check fails if no conditions are present within a rule.

Source
AWS Security Hub
Security Hub Control Id: WAF.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Password policies for IAM users should have strong configurations


### Description

 Checks if the account password policy for IAM users uses the following recommended configurations: RequireUppercaseCharacters: true, RequireLowercaseCharacters: true, RequireSymbols: true, RequireNumbers: true, MinimumPasswordLength: 8.

Source
AWS Security Hub
Security Hub control ID: IAM.7

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront SSL Certificate on the Origin Server


### Description

 Checks your origin server for SSL certificates that are expired, about to expire, missing, or that use outdated encryption. If a certificate is expired, CloudFront responds to requests for your content with HTTP status code 502, Bad Gateway. Certificates that were encrypted by using the SHA-1 hashing algorithm are being deprecated by web browsers such as Chrome and Firefox. Depending on the number of SSL certificates that you have associated with your CloudFront distributions, this check might add a few cents per month to your bill with your web hosting provider, for example, AWS if you're using EC2 or ELB as the origin for your CloudFront distribution. This check does not validate your origin certificate chain or certificate authorities; you can check these in your CloudFront configuration. 

### Alert Criteria


Red: An SSL certificate on your origin has expired or is missing.
Yellow: An SSL certificate on your origin expires in the next thirty days.
Yellow: An SSL certificate on your origin was encrypted by using the SHA-1 hashing algorithm.
Yellow: An SSL certificate on your origin can't be located. The connection might have failed due to timeout, or other HTTPS connection problems.

### Recommended Action


Renew the certificate on your origin if it has expired or is about to expire.
Add a certificate if one does not exist.
Replace a certificate that was encrypted by using the SHA-1 hashing algorithm with a certificate that is encrypted by using the SHA-256 hashing algorithm.

### Additional Resources


Using Alternate Domain Names and HTTPS

## RDS Option Groups


### Description

 Checks for usage that is more than 80% of the RDS Option Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## EBS Provisioned IOPS (SSD) Volume Aggregate IOPS


### Description

 Checks for usage that is more than 80% of the EBS Provisioned IOPS (SSD) Volume Aggregate IOPS Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## Savings Plan


### Description

 Checks your usage of EC2, Fargate, and Lambda over the last 30 days and provides Savings Plan purchase recommendations, which allows you to commit to a consistent usage amount measured in $/hour for a one or three year term in exchange for discounted rates. These are sourced from AWS Cost Explorer which can be used to get more detailed recommendation information, or to purchase a savings plan. These recommendations should be considered an alternative to your RI recommendations and choosing to act fully on both sets of recommendations would likely lead to over commitment. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account. 


### Alert Criteria



Yellow: Optimizing the purchase of Savings Plans can help reduce costs.


### Recommended Action



See the Cost Explorer page for more detailed and customized recommendations and to purchase Savings Plans. 


### Additional Resources



Savings Plan User Guide

Savings Plan FAQ

## Number of AWS Regions in an Incident Manager replication set


### Description

 Checks that an Incident Manager replication set's configuration uses more than one AWS Region to support regional failover and response. For incidents created by CloudWatch alarms or EventBridge events, Incident Manager creates an incident in the same AWS Region as the alarm or event rule. If Incident Manager is temporarily unavailable in that Region, the system attempts to create an incident in another Region in the replication set. If the replication set includes only one Region, the system fails to create an incident record while Incident Manager is unavailable.

### Alert Criteria


Green: The replication set contains more than one Region.
Yellow: The replication set contains one Region.

### Recommended Action


Add at least one more Region to the replication set.

### Additional Resources


For more information, see Cross-region Incident management.

## Application Load Balancer should be configured with defensive or strictest desync mitigation mode


### Description

 Checks if the Application Load Balancer is configured with defensive or strictest de-sync mitigation mode. This check fails if the Application Load Balancer is not configured with defensive or strictest desync mitigation mode.

Source
AWS Security Hub
Security Hub Control Id: ELB.12

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM customer managed policies should not allow decryption actions on all KMS keys


### Description

 Checks if the default version of IAM customer managed policies allow principals to use the AWS Key Management Service (KMS) decryption actions on all resources. This check fails if kms:Decrypt or kms:ReEncryptFrom actions are allowed on all KMS keys. The check evaluates both attached and unattached customer managed policies. It does not check inline policies or AWS managed policies.

Source
AWS Security Hub
Security Hub control ID: KMS.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Route 53 Reusable Delegation Sets


### Description

 Checks for usage that is more than 80% of the Route 53 Reusable Delegation Sets Limit per account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Route 53 Limits

## Classic Load Balancer should be configured with defensive or strictest desync mitigation mode


### Description

 Checks if the Classic Load Balancer is configured defensive or strictest desync mitigation mode. This check will fail if the Application Load Balancer is not configured with defensive strictest mitigation Desync mitigation mode.

Source
AWS Security Hub
Security Hub Control Id: ELB.14

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys


### Description

 Checks if the inline policies embedded in your IAM principals (Role/User/Group) allow the AWS Key Management Service (KMS) decryption actions on all KMS keys. This check fails if kms:Decrypt or kms:ReEncryptFrom actions are allowed on all KMS keys in an inline policy.

Source
AWS Security Hub
Security Hub control ID: KMS.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Kinesis streams should be encrypted at rest


### Description

 Checks if Kinesis streams are encrypted at rest with server-side encryption. This check fails if a Kinesis stream is not encrypted at rest with server-side encryption.

Source
AWS Security Hub
Security Hub Control Id: Kinesis.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS KMS keys should not be deleted unintentionally


### Description

 Checks whether AWS Key Management Service (KMS) keys are scheduled for deletion. The check fails if a KMS key is scheduled for deletion.

Source
AWS Security Hub
Security Hub control ID: KMS.3

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB Security Groups


### Description

 Checks for usage that is more than 80% of the RDS DB Security Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Network Firewall policies should have at least one rule group associated


### Description

 Checks if a Network Firewall policy has any stateful or stateless rule groups associated. This check fails if stateless or stateful rule groups are not assigned.

Source
AWS Security Hub
Security Hub Control Id: NetworkFirewall.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon SQS queues should be encrypted at rest


### Description

 Checks if Amazon SQS queues are encrypted at rest.

Source
AWS Security Hub
Security Hub control ID: SQS.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## The default stateless action for Network Firewall policies should be drop or forward for full packets


### Description

 Checks if the default stateless action for full packets for a Network Firewall policy is drop or forward. The check passes if Drop or Forward is selected, and fails if Pass is selected.

Source
AWS Security Hub
Security Hub Control Id: NetworkFirewall.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM policies should not allow full "*" administrative privileges


### Description

 Checks if the default version of AWS Identity and Access Management (IAM) policies (also known as customer managed policies) do not have administrator access with a statement that has "Effect": "Allow" with "Action": "*" over "Resource": "*". It only assesses for the Customer Managed Policies that you created, but not inline and AWS Managed Policies.

Source
AWS Security Hub
Security Hub control ID: IAM.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## The default stateless action for Network Firewall policies should be drop or forward for fragmented packets


### Description

 Checks if a Network Firewall policy has drop or forward as the default stateless action for fragmented packets. The check passes if Drop or Forward is selected, and fails if Pass is selected.

Source
AWS Security Hub
Security Hub Control Id: NetworkFirewall.5

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM users should not have IAM policies attached


### Description

 Checks that none of your IAM users have policies attached. Instead, IAM users must inherit permissions from IAM groups or roles.

Source
AWS Security Hub
Security Hub control ID: IAM.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ELB Connection Draining


### Description

 Checks for load balancers that do not have connection draining enabled. When connection draining is not enabled and you remove (deregister) an Amazon EC2 instance from a load balancer, the load balancer stops routing traffic to that instance and closes the connection. When connection draining is enabled, the load balancer stops sending new requests to the deregistered instance but keeps the connection open to serve active requests.

### Alert Criteria


 
Yellow: Connection draining is not enabled for a load balancer.
 
### Recommended Action


Enable connection draining for the load balancer. For more information, see Connection Draining and Enable or Disable Connection Draining for Your Load Balancer.

### Additional Resources


Elastic Load Balancing Concepts

## IAM users' access keys should be rotated every 90 days or less


### Description

 Checks if the active access keys are rotated within 90 days.

Source
AWS Security Hub
Security Hub control ID: IAM.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 bucket server access logging should be enabled


### Description

 Checks if an Amazon S3 Bucket has server access logging enabled to a chosen target bucket.

Source
AWS Security Hub
Security Hub Control Id: S3.9

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Stateless network firewall rule group should not be empty


### Description

 Checks if a Stateless Network Firewall Rule Group contains rules. The rule will fail if there are no rules in a Stateless Network Firewall Rule Group.

Source
AWS Security Hub
Security Hub Control Id: NetworkFirewall.6

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudTrail should have encryption at-rest enabled


### Description

 Checks whether AWS CloudTrail is configured to use the server-side encryption (SSE) AWS Key Management Service (AWS KMS) key encryption. The check will pass if the KmsKeyId is defined.

Source
AWS Security Hub
Security Hub control ID: CloudTrail.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS Reserved Instances


### Description

 Checks for usage that is more than 80% of the RDS Reserved Instances Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon EC2 instances over-provisioned for Microsoft SQL Server


### Description

 Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. An SQL Server database has a compute capacity limit for each instance. An instance with SQL Server Standard edition can use up to 48 vCPUs. An instance with SQL Server Web can use up to 32 vCPUs. This check alerts you if an instance exceeds this vCPU limit.If your instance is over-provisioned, you pay full price without realizing an improvement in performance. You can manage the number and size of your instances to help lower costs. Estimated monthly savings are calculated by using the same instance family with the maximum number of vCPUs that an SQL Server instance can use and the On-Demand pricing. Actual savings will vary if you’re using Reserved Instances (RI) or if the instance isn’t running for a full day.

### Alert Criteria


Red: An instance with SQL Server Standard edition has more than 48 vCPUs.
Red: An instance with SQL Server Web edition has more than 32 vCPUs.

### Recommended Action


For SQL Server Standard edition, consider changing to an instance in the same instance family with 48 vCPUs. For SQL Server Web edition, consider changing to an instance in the same instance family with 32 vCPUs. If it is memory intensive, consider changing to memory optimized R5 instances. For more information, see Best Practices for Deploying Microsoft SQL Server on Amazon EC2.

### Additional Resources


Microsoft SQL Server on AWS
You can use Launch Wizard to simplify your SQL Server deployment on EC2.


## IAM Roles


### Description

 Checks for usage that is more than 80% of the IAM Roles Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## CloudFront distributions should encrypt traffic to custom origins


### Description

 Checks if CloudFront distributions are encrypting traffic to custom origins. This check fails for a CloudFront distribution whose origin protocol policy allows 'http-only' or if it is 'match-viewer' and the viewer protocol policy is 'allow-all'. 

Source
AWS Security Hub
Security Hub Control Id: CloudFront.9

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudTrail trails should be integrated with Amazon CloudWatch Logs


### Description

 Checks if AWS CloudTrail trails are configured to send logs to Amazon CloudWatch Logs.

Source
AWS Security Hub
Security Hub control ID: CloudTrail.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudTrail log file validation should be enabled


### Description

 Checks if CloudTrail log file validation is enabled.

Source
AWS Security Hub
Security Hub control ID: CloudTrail.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## VPC


### Description

 Checks for usage that is more than 80% of the VPC Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

 
### Additional Resources


VPC Limits

## AWS Lambda On Failure Event Destinations


### Description

 Checks that Lambda functions in your account have On Failure event destination or Dead Letter Queue (DLQ) configured for asynchronous invocations, so that records from failed invocations can be routed to a destination for further investigation or processing.

### Alert Criteria


Yellow: Function does not have any On Failure event destination or DLQ configured.

### Recommended Action


Please set up On Failure event destination or DLQ for your lambda functions to send failed invocations along with other details to one of the available destination AWS services for further debugging or processing.

### Additional Resources


For more information, please refer to the AWS Public documentation on: Asynchronous InvocationAWS Lambda Destinations

## OpenSearch domains should have audit logging enabled


### Description

 Checks if Amazon OpenSearch Service domains have audit logging enabled.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.5

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon SageMaker notebook instances should not have direct internet access


### Description

 Checks if direct internet access is disabled for an Amazon SageMaker notebook instance by examining the DirectInternetAccess field is disabled for an Amazon SageMaker notebook instance.

Source
AWS Security Hub
Security Hub control ID: SageMaker.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## OpenSearch domain error logging to CloudWatch Logs should be enabled


### Description

 Checks if Amazon OpenSearch domains are configured to send error logs to CloudWatch Logs. This check fails if error logging to CloudWatch is not enabled for a domain.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Elastic MapReduce cluster master nodes should not have public IP addresses


### Description

 Checks if master nodes on EMR clusters have public IP addresses.

Source
AWS Security Hub
Security Hub control ID: EMR.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## OpenSearch domains should encrypt data sent between nodes


### Description

 Checks if Amazon OpenSearch domains have node-to-node encryption enabled. This check fails if node-to-node encryption is disabled on the domain.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Connections to Amazon Redshift clusters should be encrypted in transit


### Description

 Checks if connections to Amazon Redshift clusters are required to use encryption in transit. The check fails if the Amazon Redshift cluster parameter require_SSL is not set to 1.

Source
AWS Security Hub
Security Hub control ID: Redshift.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon EC2 Reserved Instances Optimization


### Description

 A significant part of using AWS involves balancing your Reserved Instance (RI) usage and your On-Demand instance usage. We provide recommendations on which RIs will help reduce costs incurred from using On-Demand instances.

AWS generates these recommendations by analyzing your On-Demand usage for the past 30 days, and then categorizing the usage into eligible categories for reservations. We then simulate every combination of reservations in the generated category of usage in order to identify the best number of each type of RI to purchase to maximize your savings. This check covers recommendations based on Standard Reserved Instances with partial upfront payment option. This check is not available to accounts linked in Consolidated Billing. Recommendations are only available for the Paying Account.


### Alert Criteria



Yellow: Optimizing the use of partial upfront RIs can help reduce costs.


### Recommended Action



See the Cost Explorer page for more detailed and customized recommendations. Additionally, refer to the buying guide to understand how to purchase RIs and the options available.


### Additional Resources



Information on RIs and how they can save you money can be found here.

For more information on this recommendation, see Reserved Instance Optimization Check Questions in the Trusted Advisor FAQs.

## OpenSearch domains should be in a VPC


### Description

 Checks Amazon OpenSearch Service domains are in an Amazon Virtual Private Cloud (VPC).

Source
AWS Security Hub
Security Hub Control Id: Opensearch.2

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Redshift clusters should prohibit public access


### Description

 Checks if Amazon Redshift clusters are publicly accessible. It evaluates the publiclyAccessible field in the cluster configuration item.

Source
AWS Security Hub
Security Hub control ID: Redshift.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## OpenSearch domains should have encryption at rest enabled


### Description

 Checks if Amazon OpenSearch domains have encryption-at-rest configuration enabled. The check fails if encryption at rest is not enabled.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.1

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Redshift clusters should use enhanced VPC routing


### Description

 Checks if a Redshift cluster has EnhancedVpcRouting enabled.

Source
AWS Security Hub
Security Hub control ID: Redshift.7

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon EFS No Mount Target Redundancy


### Description

 Checks if mount targets exist in multiple Availability Zones for an Amazon EFS file system.

### Alert Criteria


Yellow: File system has 1 mount target created in a single Availability Zone.
Green: File system has 2 or more mount targets created in multiple Availability Zones.

### Recommended Action


For EFS file systems using One Zone storage classes, we recommend you create new file systems that use Standard storage classes by restoring a backup to a new file system. Then create mount targets in multiple Availability Zones. For EFS file systems using Standard storage classes, we recommend you create mount targets in multiple Availability Zones.

### Additional Resources


For more information, see Managing mount targets using the Amazon EFS console and  Amazon EFS Quotas and Limits.

## Amazon EC2 instances launched using Auto Scaling group launch configurations should not have Public IP addresses


### Description

 Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled using launch configurations.

Source
AWS Security Hub
Security Hub Control Id: Autoscaling.5

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Redshift should have automatic upgrades to major versions enabled


### Description

 Checks if an Amazon Redshift cluster is configured with automatic upgrades to major versions.

Source
AWS Security Hub
Security Hub control ID: Redshift.6

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon EFS Throughput Mode Optimization


### Description

 Checks whether the customer's Amazon EFS file system is currently configured to use Bursting Throughput mode. File systems in EFS's Bursting Throughput mode [1] deliver a consistent baseline level of throughput (50 KiB/s per GiB of data in EFS Standard storage), and use a credit model to deliver higher levels of "burst throughput" performance when "burst credits" are available. When you exhaust your burst credits, your file system performance is throttled to this lower, baseline level, which can result in slowness, timeouts, or other forms of performance impact for your end users or applications.

### Alert Criteria


Yellow: File system is using Bursting throughput mode.

### Recommended Action


To allow your users and applications to achieve their desired throughput, we recommend that you update your file system configuration to Elastic Throughput mode [2]. When in Elastic Throughput mode, your file system can achieve up to 10 GiB/s of read throughput or 3 GiB/s of write throughput - depending on the AWS Region [3], and you only pay for the throughput you use. Please note that you can update your file system configuration to switch between Elastic and Bursting throughput modes on demand, and that File Systems in Elastic Throughput mode accrue additional charges for data transfer [4].

### Additional Resources


For more information, see [1] Amazon EFS Performance Throughput Modes, [2] Amazon EFS Performance Elastic Throughput Mode, [3] Amazon EFS Quotas and Limits, and [4] Amazon EFS Pricing.

## CloudFront distributions should use custom SSL/TLS certificates


### Description

 Checks if CloudFront distributions are using the default SSL/TLS certificate CloudFront provides instead of a custom one. This check fails for a CloudFront distribution if it uses the default SSL/TLS certificate.

Source
AWS Security Hub
Security Hub Control Id: CloudFront.7

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Redshift clusters should have audit logging enabled


### Description

 Checks if an Amazon Redshift cluster has audit logging enabled.

Source
AWS Security Hub
Security Hub control ID: Redshift.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should use SNI to serve HTTPS requests


### Description

 Checks if Amazon CloudFront distributions are using a custom SSL/TLS certificate and are configured to use SNI to serve HTTPS requests as opposed to dedicated IP address.

Source
AWS Security Hub
Security Hub Control Id: CloudFront.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should require encryption in transit


### Description

 Checks if an Amazon CloudFront distribution requires viewers to use HTTPS directly, or if it uses redirection. The check fails if ViewerProtocolPolicy is set to allow-all for defaultCacheBehavior or for cacheBehaviors.

Source
AWS Security Hub
Security Hub control ID: CloudFront.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## VPN Tunnel Redundancy


### Description

 Checks the number of tunnels that are active for each of your VPNs. A VPN should have two tunnels configured at all times to provide redundancy in case of outage or planned maintenance of the devices at the AWS endpoint. For some hardware, only one tunnel is active at a time (see the Amazon Virtual Private Cloud Network Administrator Guide). If a VPN has no active tunnels, charges for the VPN might still apply.

### Alert Criteria


Yellow: A VPN has one active tunnel (this is normal for some hardware).
Yellow: A VPN has no active tunnels.

### Recommended Action


Be sure that two tunnels are configured for your VPN connection, and that both are active if your hardware supports it. If you no longer need a VPN connection, you can delete it to avoid charges. For more information, see Your Customer Gateway or Deleting a VPN connection.

### Additional Resources


Amazon Virtual Private Cloud Network Administrator Guide
Adding a Hardware Virtual Private Gateway to Your VPC

## Secrets should not be passed as container environment variable


### Description

 Checks if the container environment variables includes the following keys - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,  or ECS_ENGINE_AUTH_DATA.

Source
AWS Security Hub
Security Hub Control Id: ECS.8

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Stopped EC2 instances should be removed after a specified time period


### Description

 Checks if any EC2 instances have been stopped for more than the allowed number of days. An EC2 instance fails this check if it is stopped for longer than the maximum allowed time period, which by default is 30 days.

Source
AWS Security Hub
Security Hub control ID: EC2.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECR private repositories should have image scanning enabled


### Description

 Checks if a private ECR repository has image scanning enabled. This check fails if a private ECR repository has image scanning disabled. Amazon ECR image scanning helps in identifying software vulnerabilities in your container images. Amazon ECR uses the Common Vulnerabilities and Exposures (CVEs) database from the open-source Clair project and provides a list of scan findings. Enabling image scanning on ECR repositories adds a layer of verification for the integrity and safety of the images being stored.

Source
AWS Security Hub
Security Hub Control Id: ECR.1

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EBS default encryption should be enabled


### Description

 Checks if Amazon Elastic Block Store (EBS) encryption is enabled by default. The check fails if EBS default encryption is not enabled.

Source
AWS Security Hub
Security Hub control ID: EC2.7

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EBS volumes should be attached to EC2 instances


### Description

 Checks if EBS volumes are attached to EC2 instances.

Source
AWS Security Hub
Security Hub control ID: EC2.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS Direct Connect Virtual Interface Redundancy


### Description

 Checks for virtual private gateways with Direct Connect virtual interfaces (VIFs) that are not configured on at least two Direct Connect connections. Connectivity to your virtual private gateway should have multiple virtual interfaces configured across multiple Direct Connect connections and locations to provide redundancy in case a device or location is unavailable. 
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow:  A virtual private gateway has less than two virtual interfaces, or the interfaces are not configured to multiple Direct Connect connections. 

### Recommended Action


Configure at least two virtual interfaces that are configured to two Direct Connect connections to protect against device or location unavailability. See Create a Virtual Interface.

### Additional Resources


Getting Started with AWS Direct Connect
AWS Direct Connect FAQs 

Working With AWS Direct Connect Virtual Interfaces

## RDS Database Clusters should use a custom administrator username


### Description

 Checks if an RDS database cluster has changed the admin username from its default value. This rule will fail if the admin username is set to the default value.

Source
AWS Security Hub
Security Hub Control Id: RDS.24

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudTrail should be enabled and configured with at least one multi-region trail


### Description

 Checks that there is at least one multi-region AWS CloudTrail trail.

Source
AWS Security Hub
Security Hub control ID: CloudTrail.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS database instances should use a custom administrator username


### Description

 Checks if an Amazon Relational Database Service (Amazon RDS) database instance has changed the admin username from its default value. This rule will only run on RDS database instances. The rule will fail if the admin username is set to the default value.

Source
AWS Security Hub
Security Hub Control Id: RDS.25

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Secrets Manager secrets should be rotated within a specified number of days


### Description

 Checks if your secrets have rotated at least once within 90 days.

Source
AWS Security Hub
Security Hub control ID: SecretsManager.4

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## AWS CodeBuild S3 Logs should be encrypted


### Description

 Checks if a AWS CodeBuild project configured with Amazon S3 Logs has encryption enabled for its logs.

Source
AWS Security Hub
Security Hub Control Id: CodeBuild.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Secrets Manager secrets configured with automatic rotation should rotate successfully


### Description

 Checks if an AWS Secrets Manager secret rotated successfully based on the rotation schedule. The check fails if RotationOccurringAsScheduled is false. The check does not evaluate secrets that do not have rotation configured.

Source
AWS Security Hub
Security Hub control ID: SecretsManager.2

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECR private repositories should have tag immutability enabled


### Description

 Checks if a private ECR repository has tag immutability enabled. This check fails if a private ECR repository has tag immutability disabled.

Source
AWS Security Hub
Security Hub Control Id: ECR.2

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Remove unused Secrets Manager secrets


### Description

 Checks if your secrets have been accessed within a specified number of days. The default value is 90 days. Secrets that have not been accessed even once within the number days you define, fail this check.

Source
AWS Security Hub
Security Hub control ID: SecretsManager.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ActiveMQ Availability Zone Redundancy.


### Description

 Checks that Amazon MQ for ActiveMQ brokers are configured for high availability with an active/standby broker in multiple Availability Zones.

### Alert Criteria


Green: An Amazon MQ for ActiveMQ broker is configured in at least two Availability Zones.
Yellow: An Amazon MQ for ActiveMQ broker is configured in a single Availability Zone.

### Recommended Action


Create a new broker with active/standby deployment mode.

### Additional Resources


For more information, see Creating an ActiveMQ broker..

## Amazon ECS Task Definitions should not share the host's process namespace


### Description

 Checks if Amazon ECS Task Definitions are configured to share a host's process namespace with its containers.

Source
AWS Security Hub
Security Hub Control Id: ECS.3

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Secrets Manager secrets should have automatic rotation enabled


### Description

 Checks if a secret stored in AWS Secrets Manager is configured to rotate automatically.

Source
AWS Security Hub
Security Hub control ID: SecretsManager.1

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS DB Parameter Groups


### Description

 Checks for usage that is more than 80% of the RDS DB Parameter Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## Amazon ECS Containers should run as non-privileged


### Description

 Checks if the Privileged parameter in the container definition of Amazon ECS Task Definitions is set to 'true'.

Source
AWS Security Hub
Security Hub Control Id: ECS.4

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EBS snapshots should not be public, determined by the ability to be restorable by anyone


### Description

 Checks if Amazon Elastic Block Store snapshots are not publicly restorable.

Source
AWS Security Hub
Security Hub control ID: EC2.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon ECS Containers should only have read-only access to its root filesystems


### Description

 Checks if ECS Containers are limited to read-only access to its mounted root filesystems.

Source
AWS Security Hub
Security Hub Control Id: ECS.5

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Attached EBS volumes should be encrypted at-rest


### Description

 Checks if the EBS volumes that are in an attached state are encrypted.

Source
AWS Security Hub
Security Hub control ID: EC2.3

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## RDS Subnet Groups


### Description

 Checks for usage that is more than 80% of the RDS Subnet Groups Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


RDS Limits

## RabbitMQ Availability Zone Redundancy. 


### Description

 Checks that Amazon MQ for RabbitMQ brokers are configured for high availability with cluster instances in multiple Availability Zones.

### Alert Criteria


Green: An Amazon MQ for RabbitMQ broker is configured in multiple Availability Zones.
Yellow: An Amazon MQ for RabbitMQ broker is configured in a single Availability Zone.

### Recommended Action


Create a new broker with the cluster deployment mode.

### Additional Resources


For more information, see Creating a RabbitMQ broker..

## The VPC default security group should not allow inbound and outbound traffic


### Description

 Checks that the default security group of a VPC does not allow inbound or outbound traffic.

Source
AWS Security Hub
Security Hub control ID: EC2.2

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon MemoryDB Multi-AZ clusters


### Description

 Checks for MemoryDB clusters that deploy in a single Availability Zone (AZ). This check alerts you if Multi-AZ is inactive in a cluster.

Deployments in multiple AZs enhance MemoryDB cluster availability by asynchronously replicating to read-only replicas in a different AZ. When planned cluster maintenance occurs, or a primary node is unavailable, MemoryDB automatically promotes a replica to primary. This failover allows cluster write operations to resume, and doesn't require an administrator to intervene.

### Alert Criteria


Green: Multi-AZ is active in the cluster.
Yellow: Multi-AZ is inactive in the cluster.

### Recommended Action


Create at least one replica per shard, in an AZ that is different than the primary.

Additional Information
For more information, see Minimizing downtime in MemoryDB with Multi-AZ.


## EC2 On-Demand Instances


### Description

 Checks for usage that is more than 80% of the EC2 On-Demand Instances Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EC2 Limits

## Amazon EC2 to EBS Throughput Optimization


### Description

 Checks for Amazon EBS volumes whose performance might be affected by the maximum throughput capability of the Amazon EC2 instance they are attached to. 

To optimize performance, you should ensure that the maximum throughput of an EC2 instance is greater than the aggregate maximum throughput of the attached EBS volumes. 

This check computes the total EBS volume throughput for each five-minute period in the preceding day (UTC) for each EBS-optimized instance and alerts you if usage in more than half of those periods was greater than 95% of the maximum throughput of the EC2 instance.
 

### Alert Criteria


 Yellow: In the preceding day (UTC), the aggregate throughput (megabytes/sec) of the EBS volumes attached to the EC2 instance exceeded 95% of the published throughput between the instance and the EBS volumes more than 50% of time.
 

### Recommended Action


 Compare the maximum throughput of your EBS volumes 

(see Amazon EBS Volume Types) 

with the maximum throughput of the EC2 instance they are attached to 

(see Instance Types That Support EBS Optimization). 

Consider attaching your volumes to an instance that supports higher throughput to EBS for optimal performance.
 

### Additional Resources


Amazon EBS Volume Types
 

Amazon EBS-Optimized Instances
 

Monitoring the Status of Your Volumes
 

Attaching an Amazon EBS Volume to an Instance
 

Detaching an Amazon EBS Volume from an Instance
 

Deleting an Amazon EBS Volume 

## Amazon ElastiCache Multi-AZ clusters


### Description

 Checks for ElastiCache clusters that deploy in a single Availability Zone (AZ). This check alerts you if Multi-AZ is inactive in a cluster.

Deployments in multiple AZs enhance ElastiCache cluster availability by asynchronously replicating to read-only replicas in a different AZ. When planned cluster maintenance occurs, or a primary node is unavailable, ElastiCache automatically promotes a replica to primary. This failover allows cluster write operations to resume, and doesn't require an administrator to intervene.

### Alert Criteria


Green: Multi-AZ is active in the cluster.
Yellow: Multi-AZ is inactive in the cluster.

### Recommended Action


Create at least one replica per shard, in an AZ that is different than the primary.

Additional Information
For more information, see Minimizing downtime in ElastiCache with Multi-AZ.

## EC2 subnets should not automatically assign public IP addresses


### Description

 Checks if the assignment of public IPs in Amazon Virtual Private Cloud (VPC) subnets have the MapPublicIpOnLaunch set to FALSE. The check will pass if the flag is set to FALSE.

Source
AWS Security Hub
Security Hub control ID: EC2.15

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 instances should not use multiple ENIs


### Description

 Checks to see if Amazon EC2 instance uses multiple ENI/EFA. This check will pass if single network adapters is used.

Source
AWS Security Hub
Security Hub control ID: EC2.17

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Unused Network Access Control Lists should be removed


### Description

 Checks to see if there are any NACLs (Network Access Control List) that are unused. The check will check the item configuration of the resource AWS::EC2::NetworkAcl and determine the relationships of the NACL.

Source
AWS Security Hub
Security Hub control ID: EC2.16

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## EC2 Reserved Instance Leases


### Description

 Checks for usage that is more than 80% of the EC2 Reserved Instance Leases Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EC2 Limits

## CloudFront distributions should have a default root object configured


### Description

 Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object. The check fails if the CloudFront distribution does not have a default root object configured.

Source
AWS Security Hub
Security Hub control ID: CloudFront.1

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CloudFront distributions should have WAF enabled


### Description

 Checks to see if Amazon CloudFront distributions are associated with either WAF or WAFv2 web ACLs. The check fails if a CloudFront distribution is not associated with a web ACL.

Source
AWS Security Hub
Security Hub control ID: CloudFront.6

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## API Gateway REST API cache data should be encrypted at rest


### Description

 Checks if all methods in Amazon API Gateway REST API stages that have cache enabled are encrypted. The check fails if any method in API Gateway REST API stage is configured to cache and the cache is not encrypted.

Source
AWS Security Hub
Security Hub control ID: APIGateway.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Elasticsearch Service domains should have audit logging enabled


### Description

 This check checks whether Amazon Elasticsearch Service domains have audit logging enabled. This check fails if an Amazon Elasticsearch Service domain does not have audit logging enabled.

Source
AWS Security Hub
Security Hub control ID: ES.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Security groups should not allow unrestricted access to ports with high risk


### Description

 Checks if unrestricted incoming traffic for the security groups is accessible to the specified ports [3389, 20, 23, 110, 143, 3306, 8080, 1433, 9200, 9300, 25, 445, 135, 21, 1434, 4333, 5432, 5500, 5601, 22 ] that have the highest risk. This check passes when none of the rules in a security group allow ingress traffic from 0.0.0.0/0 for the listed ports.

Source
AWS Security Hub
Security Hub control ID: EC2.19

### Alert Criteria


Red: Critical or High. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Classic Load Balancers with HTTPS/SSL listeners should use a predefined security policy that has strong configuration


### Description

 Checks if your Classic Load Balancer SSL listeners use the predefined policy ELBSecurityPolicy-TLS-1-2-2017-01. The check fails if the Classic Load Balancer SSL listeners do not use the predefined policy ELBSecurityPolicy-TLS-1-2-2017-01.

Source
AWS Security Hub
Security Hub control ID: ELB.8

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Amazon Route 53 Latency Resource Record Sets


### Description

 Checks for Amazon Route 53 latency record sets that are configured inefficiently. To allow Amazon Route 53 to route queries to the region with the lowest network latency, you should create latency resource record sets for a particular domain name (such as example.com) in different regions. If you create only one latency resource record set for a domain name, all queries are routed to one region, and you pay extra for latency-based routing without getting the benefits. Hosted zones created by AWS services won’t appear in your check results.


### Alert Criteria



Yellow: Only one latency resource record set is configured for a particular domain name.


### Recommended Action



If you have resources in multiple regions, be sure to define a latency resource record set for each region; see Latency-Based Routing.
If you have resources in only one region, consider creating resources in more than one region and define latency resource record sets for each; see Latency-Based Routing.
If you don't want to use multiple regions, you should use a simple resource record set; see  Working with Resource Record Sets.


### Additional Resources



Amazon Route 53 Developer Guide
Amazon Route 53 Pricing

## Amazon EC2 should be configured to use VPC endpoints that are created for the Amazon EC2 service


### Description

 Checks if a service endpoint for Amazon EC2 is created for each VPC. The check fails if a VPC does not have a VPC endpoint created for the Amazon EC2 service.

Source
AWS Security Hub
Security Hub control ID: EC2.10

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## SES Daily Sending Quota


### Description

 Checks for usage that is more than 80% of the SES Daily Sending Quota Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


SES Limits

## EBS General Purpose SSD (gp3) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS General Purpose SSD (gp3) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## EBS General Purpose SSD (gp2) Volume Storage


### Description

 Checks for usage that is more than 80% of the EBS General Purpose SSD (gp2) Volume Storage Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


EBS Limits

## IAM Use


### Description

 This check is intended to discourage the use of root access by checking for existence of at least one IAM user. You may ignore the alert if you are following the best practice of centralizing identities and configuring users in an external identity provider or AWS Single Sign-On. 


### Alert Criteria


Yellow: No IAM users have been created for this account.


### Recommended Action


Create an IAM user or use AWS Single Sign-On to create additional users whose permissions are limited to perform specific tasks in your AWS environment. 

### Additional Resources


What is AWS Single Sign-On?
What Is IAM?

## AWS Direct Connect Location Redundancy


### Description

 Checks for regions with one or more AWS Direct Connect connections and only one AWS Direct Connect location. Connectivity to your AWS resources should have Direct Connect connections configured to different Direct Connect locations to provide redundancy in case a location is unavailable.
Note: Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

### Alert Criteria


Yellow:  The Direct Connect connections in the region are not configured to different locations.

### Recommended Action


Configure a Direct Connect connection that uses a different Direct Connect location to protect against location unavailability. For more information, see Getting Started with AWS Direct Connect.

### Additional Resources


Getting Started with AWS Direct Connect
AWS Direct Connect FAQs

## Connections to OpenSearch domains should be encrypted using TLS 1.2


### Description

 Checks if connections to OpenSearch domains are required to use TLS 1.2. The check fails if the OpenSearch domain TLSSecurityPolicy is not Policy-Min-TLS-1-2-2019-07.

Source
AWS Security Hub
Security Hub Control Id: Opensearch.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## CodeBuild project environments should not have privileged mode enabled


### Description

 Checks if an AWS CodeBuild project environment has privileged mode enabled.

Source
AWS Security Hub
Security Hub Control Id: CodeBuild.5

### Alert Criteria


Red: Critical or High Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM Password Policy


### Description

 Checks the password policy for your account and warns when a password policy is not enabled, or if password content requirements have not been enabled. Password content requirements increase the overall security of your AWS environment by enforcing the creation of strong user passwords. When you create or change a password policy, the change is enforced immediately for new users but does not require existing users to change their passwords. 


### Alert Criteria


Yellow: A password policy is enabled, but at least one content requirement is not enabled.  

Red: No password policy is enabled. 


### Recommended Action


If some content requirements are not enabled, consider enabling them. If no password policy is enabled, create and configure one. See Setting an Account Password Policy for IAM Users. 


### Additional Resources


Managing Passwords

## Amazon Redshift clusters should not use the default Admin username


### Description

 Checks if a Redshift cluster has changed the Admin username from its default value. This check will fail if the admin username for a Redshift cluster is set to 'awsuser'.

Source
AWS Security Hub
Security Hub Control Id: Redshift.8

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Route 53 Traffic Policy Instances


### Description

 Checks for usage that is more than 80% of the Route 53 Traffic Policy Instances Limit per account. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


Route 53 Limits

## Amazon Route 53 MX Resource Record Sets and Sender Policy Framework


### Description

 For each MX resource record set, checks that the TXT or SPF resource record set contains a valid SPF record. The record must start with "v=spf1". The SPF record specifies the servers that are authorized to send email for your domain, which helps detect and stop email address spoofing to reduce spam. Route 53 recommends that you use a TXT record instead of an SPF record. Trusted Advisor reports this check as green as long as each MX resource record set has at least one SPF or TXT record.


### Alert Criteria



Yellow: An MX resource record set doesn’t have a TXT or SPF resource record that contains a valid SPF value.

### Recommended Action



For each MX resource record set, create a TXT resource record set that contains a valid SPF value. For more information, see Sender Policy Framework: SPF Record Syntax and Creating Resource Record Sets By Using the Amazon Route 53 Console.

Additional Information

Sender Policy Framework (Wikipedia)
MX record (Wikipedia)

## Amazon EC2 instances with Microsoft Windows Server end of support


### Description

 This check alerts you if the versions are near or have reached the end of support. Each Windows Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support.  After the end of support, the Windows Server version won’t receive regular security updates. Running applications with unsupported Windows Server versions can bring security or compliance risks.

### Alert Criteria


Red: An EC2 instance has a Windows Server version that has reached end of support (Windows Server 2003, 2008, and 2008R2)
Yellow: An EC2 instance has a Windows Server version that will reach end of support in less than 18 months (Windows Server 2012 & 2012 R2)

### Recommended Action


Consider the following guidelines for end of support Windows Server EC2 instances:

To modernize your Windows Server workloads, consider the various pathways available on the Modernize Windows Workloads with AWS website.

To upgrade your Windows Server workloads onto modern versions of Windows Server, consider using an automation runbook to simplify your upgrade. For more information, see the AWS Systems Manager documentation.

If you can’t upgrade your Windows Server workloads due to application incompatibilities, consider the End-of-Support Migration Program (EMP) for Windows Server. For more information on the program and tooling, see the EMP website. You can also purchase Extended Security Updates (ESU) from Microsoft for a maximum of 3 years after a product’s end of support date. Learn more.


## Amazon EC2 instances with Microsoft SQL Server end of support


### Description

 Checks the SQL Server versions for Amazon Elastic Compute Cloud (Amazon EC2) instances running in the past 24 hours. This check alerts you if the versions are near or have reached the end of support. Each SQL Server version offers 10 years of support, including 5 years of mainstream support and 5 years of extended support. After the end of support, the SQL Server version won’t receive regular security updates. Running applications with unsupported SQL Server versions can bring security or compliance risks.

### Alert Criteria


Red: An EC2 instance has an SQL Server version that reached the end of support.
Yellow: An EC2 instance has an SQL Server version that will reach the end of support in 12 months.

### Recommended Action


To modernize your SQL Server workloads, consider refactoring to AWS Cloud native databases like Amazon Aurora. For more information, see Modernize Windows Workloads with AWS.
To move to a fully managed database, consider replatforming to Amazon Relational Database Service (Amazon RDS). For more information, see RDS for SQL Server.
To upgrade your SQL Server on EC2, consider using the automation runbook to simplify your upgrade. For more information, see the AWS Systems Manager documentation.
If you can’t upgrade your SQL Server on EC2, consider the End-of-Support Migration Program (EMP) for Windows Server. For more information, see the EMP Website

### Additional Resources


Get ready for SQL Server end of support with AWS
Microsoft SQL Server on AWS


## Amazon EC2 instances consolidation for Microsoft SQL Server


### Description

 Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. This check alerts you if your instance has less than the minimum number of SQL Server licenses. From the Microsoft SQL Server Licensing Guide, you are paying 4 vCPU licenses even if an instance has only 1 or 2 vCPUs. You can consolidate smaller SQL Server instances to help lower costs.

### Alert Criteria


Yellow: An instance with SQL Server has less than 4 vCPUs.

### Recommended Action


Consider consolidating smaller SQL Server workloads into instances with at least 4 vCPUs.

### Additional Resources


Microsoft SQL Server on AWS
Microsoft Licensing on AWS
Microsoft SQL Server Licensing Guide


## CloudFront distributions should have logging enabled


### Description

 Checks to see if server access logging is enabled on Amazon CloudFront Distributions. The check will fail if access logging is not enabled for the distribution.

Source
AWS Security Hub
Security Hub control ID: CloudFront.5

### Alert Criteria


Yellow: Medium or Low. Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets with versioning enabled should have lifecycle policies configured


### Description

 Checks if Amazon Simple Storage Service (Amazon S3) version enabled buckets have lifecycle policy configured. This rule fails if Amazon S3 lifecycle policy is not enabled.

Source
AWS Security Hub
Security Hub Control Id: S3.10

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 buckets should have event notifications enabled


### Description

 Checks if S3 Event Notifications are enabled on an S3 bucket. This check fails if S3 Event Notifications are not enabled on a bucket.

Source
AWS Security Hub
Security Hub Control Id: S3.11

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## S3 access control lists (ACLs) should not be used to manage user access to buckets


### Description

 Checks if S3 buckets allow user permissions via access check lists (ACLs). This check fails if ACLs are configured for user access on S3 Bucket.

Source
AWS Security Hub
Security Hub Control Id: S3.12

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Network ACLs should not allow ingress from 0.0.0.0/0 to port 22 or port 3389


### Description

 Checks if a network access check list (NACL) allows unrestricted access to the default ports for SSH/RDP ingress traffic. The rule fails if a NACL inbound entry allows a source CIDR block of '0.0.0.0/0' or '::/0' for ports 22 or 3389

Source
AWS Security Hub
Security Hub Control Id: EC2.21

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## Unused EC2 security groups should be removed


### Description

 Checks that security groups are attached to Amazon EC2 instances or to an elastic network interface. The check will fail the security group is not associated with an Amazon EC2 instance or an elastic network interface.

Source
AWS Security Hub
Security Hub Control Id: EC2.22

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## ECR repositories should have at least one lifecycle policy configured


### Description

 Checks if an ECR repository has at least one lifecycle policy configured. This check fails if an ECR repository does not have any lifecycle policies configured.

Source
AWS Security Hub
Security Hub Control Id: ECR.3

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.

## IAM Users


### Description

 Checks for usage that is more than 80% of the IAM Users Limit. Values are based on a snapshot, so your current usage might differ. Limit and usage data can take up to 24 hours to reflect any changes. In cases where limits have been recently increased, you may temporarily see utilization that exceeds the limit.

### Alert Criteria


Yellow: 80% of limit reached.
Red: 100% of limit reached.
Blue: Trusted Advisor was unable to retrieve utilization or limits in one or more regions.

### Recommended Action


If you expect to exceed a service limit, request an increase directly from the Service Quotas console. If Service Quotas doesn’t support your service yet, you can create a support case in Support Center.

### Additional Resources


IAM Limits

## CodeBuild project environments should have a logging configuration


### Description

 Checks if a CodeBuild project environment has at least one log option enabled.

Source
AWS Security Hub
Security Hub Control Id: CodeBuild.4

### Alert Criteria


Yellow: Medium or Low Security Hub control failed.

### Recommended Action


Follow the Security Hub documentation to fix the issue.
