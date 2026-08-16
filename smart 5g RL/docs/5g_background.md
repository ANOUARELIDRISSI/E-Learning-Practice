# 5G Background Notes

## Service Classes

## eMBB

Enhanced Mobile Broadband.

Typical characteristics:

- High data rate demand
- Throughput-centric objective
- Moderate latency sensitivity

Example applications:

- Video streaming
- Cloud gaming
- Large file downloads

## URLLC

Ultra-Reliable Low-Latency Communications.

Typical characteristics:

- Very strict latency targets
- Reliability-critical
- Often small packets but strict deadlines

Example applications:

- Industrial automation
- Autonomous systems
- Mission-critical communication

## mMTC

Massive Machine-Type Communications.

Typical characteristics:

- Very large number of devices
- Small and sporadic traffic
- Scalability and access efficiency are key

Example applications:

- IoT sensors
- Smart meters
- Environmental telemetry

## Fundamental Concepts

## Network Slicing

Logical partitioning of network resources to support heterogeneous services with different SLAs over shared infrastructure.

## QoS

Quality of Service metrics and constraints controlling user-perceived performance.

## Throughput

Amount of successfully delivered data per unit time.

## Latency

End-to-end delay from transmission to reception.

## Packet Loss

Fraction of packets that are dropped or not delivered successfully.

## Why Resource Allocation is Hard

- Limited shared radio resources
- Time-varying traffic and channels
- Conflicting objectives among service classes
- Need to optimize average performance while guaranteeing tails and constraints
