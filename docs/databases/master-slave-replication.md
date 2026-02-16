# Master-Slave Replication

## Overview
Master-slave replication is a database replication pattern where one database server (master) handles writes and replicates changes to one or more read-only servers (slaves). It enables read scaling and provides backup capabilities.

## Definition
Master-slave replication has a single master database that accepts writes and replicates all changes to one or more slave databases. Slaves are read-only and used for read operations, providing read scaling and high availability.

## Key Concepts

- **Master**: Single write database
- **Slaves**: Read-only replica databases
- **One-way Replication**: Replication from master to slaves
- **Read Scaling**: Scale reads with multiple slaves
- **Write Concentration**: All writes go to master
- **Failover**: Promote slave to master on failure
- **Replication Lag**: Delay in slave updates

## How It Works

Master-slave replication:

1. **Write to Master**: All writes go to master
2. **Change Logging**: Master logs changes
3. **Replication**: Changes replicated to slaves
4. **Slave Application**: Slaves apply changes
5. **Read Distribution**: Reads distributed to slaves
6. **Lag Monitoring**: Monitor replication lag
7. **Failover**: Failover to slave if master fails

Characteristics:
- **Simple**: Simple replication model
- **Read Scaling**: Scales reads
- **Single Master**: Single point for writes
- **Failover**: Can failover to slave

## Use Cases

- **Read Scaling**: Scaling read operations
- **Backup**: Maintaining backup copies
- **Analytics**: Using slaves for analytics
- **High Availability**: High availability setup
- **Geographic Distribution**: Multi-region reads

## Considerations

- **Master Bottleneck**: Master can be bottleneck
- **Replication Lag**: Lag between master and slaves
- **Failover Complexity**: Failover procedures
- **Single Master**: Single point of failure for writes

## Best Practices

- **Monitor Lag**: Track replication lag
- **Plan Failover**: Plan failover procedures
- **Balance Load**: Balance read load across slaves
- **Test Failover**: Regularly test failover
- **Optimize Replication**: Optimize replication performance

## Related Topics

- [Master-Master Replication](master-master-replication.md)
- [Database Replication](../ingestion/database-replication.md)
- [High Availability](../advanced/high-availability.md)
- Read Scaling
- Failover

---

**Category**: Database Types & Technologies  
**Last Updated**: 2024
