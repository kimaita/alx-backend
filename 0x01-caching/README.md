# Caching

Caching improves performance by keeping recent or often-used data items in memory locations which are faster,
or computationally cheaper to access, than normal memory stores.
Cache replacement policies (cache algorithms) are algorithms which a computer program or hardware-maintained structure
can utilize to manage a cache of information. When the cache is full, the algorithm must choose which items to discard to make room for new data.

We look at some cache replacement policies:

## Simple queue-based policies

- FIFO: First In First Out
  > Evicts blocks in the order in which they were added, as in a _queue_.
- LIFO: Last In First Out
  > Evicts the block added most recently first, as in a _stack_.

## Simple recency-based policies

- MRU: Most Recently Used
  > Discards the most-recently-used items first.
- LRU: Least Recently Used
  > Discards least recently used items first.

## Simple frequency-based policies

- LFU: Least Frequently Used
  > Discards less often accessed items first.
