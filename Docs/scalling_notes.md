Current Design Assumptions 

> Input is batch CSV

> Data fits in memory

> Single-node execution

> File-based state

> No concurrency




What Breaks at 10× Scale

> Memory pressure during deduplication

> Slower validation loops

> Log volume explosion

> File I/O becoming bottleneck



What Breaks at 100× Scale

> In-memory sets fail

> Single-machine throughput collapses

> CSV becomes unusable

> Re-runs become expensive

> Single log file is useless




Batch → Streaming Transition

> CSV ingestion → Kafka topic

> File-based batches → event streams

> Deduplication → windowed/stateful processing

> Metrics → continuous aggregation




What I Would Change First

> Replace CSV with columnar format

> Externalize state

> Introduce distributed processing

> Centralize metrics



What I Would Keep As-Is

> Validation logic

> Error classification

> Safe-write strategy

> Config-driven execution


