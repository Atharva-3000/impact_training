# AVL TREE
It is defined as self balancing binary search tree.

Where the difference between heights of the left and right subtrees from any node cannot be more than 1.

The difference between heights of the left and right subtree for any node is known as balance factor of the node.

### Various operations on the AVL Tree:
1. Insertion: 
2. Deletion
3. Searching: It will be similar to search operation in BST.

### Various Rotations on AVL Tree:
1. Left Rotation: 
    When the node is added into the right subtree of the right subtree, if the tree is thrown out of the balance, we do a single left rotation.
2. Right Rotation:
    When the node is added into the left subtree of the left subtree, if the tree is thrown out of the balance, we do a single right rotation.

3. Left Right Rotation: It is a combination in which the first, the `left` rotation takes place and then a `right` rotation takes place

4. Right Left Rotation: It is a combination in which the first, the `right` rotation takes place and then a `left` rotation takes place.

## Applications:
1. It is used to index records in a database and also to efficiently search in that.

2. For all types of in-memory collections, including sets and dictionary, AVL trees are used.

3. Database applications where insertions and deletions are less common but frequent data lookups are necessary.

4. Software that needs optimized search.

## Disadvantages:
1. Difficult to implement.

2. It has high constant factors for some of the operations.

3. Takes more processing time for balancing.

4. Less used to compared to red-black trees.

5. Due to its rather strict balance, AVL trees provide complicated insertions and deletion operations, as more rotations are performed.