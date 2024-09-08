# directoryComparator

This script is used to compare two directories. 

1) It skips some unsynchronized folders through the hierarchical traversal method to avoid traversing the contents of unsynchronized folders to achieve a pruning effect (it takes me an entire night to finish). 
   
2) Referring to an ACM expert's algorithm for comparing version numbers, this script uses the ``list. pop (0)`` in the middle procedure and the ``not any`` in the end procedure to accelerate the operation (it takes me about ten minutes to finish). 

3) Report relative paths about added, removed, conflicted, erroneous, and different items (it takes me about a minute to finish). 

4) This script compares file contents using SHA256 hash values instead of comparing each byte to speed up. Although both methods require traversing entire files, the method of using hash functions saves time by reducing the number of ``if`` executions (it takes me a minute to finish). 

5) This script provides a multi-level progress report structure (it seems that this feature takes me the same amount of time as the sum of the previous four points).

## v1.0

The initial version of ``compareDirectory.py``. 

It can run on Linux but does not support Linux totally. 

## v2.0

The comparison for Linux operating systems is supported. 

Each soft link is regarded as a normal file during the comparison. 

The situation that the operating system is case sensitive but the switch of case sensitive is turned off manually is considered. 

## v3.0

The script is reconstructed using multiple classes. 

A switch to indicate whether the soft links should be enabled is provided for non-Windows systems. 

The language is unified. All prompts for interactions are in English. 
