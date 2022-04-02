import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

RANDOM_STATE = 2020


def create_datasets():
    """Create train and test datasets from the same distribution

    Returns:
        (np.array, np.array, np.array, np.array):
            A tuple (X_train, X_test, y_train, y_test)
    """
    rng = np.random.default_rng(RANDOM_STATE)
    X = rng.normal(size=(160, 10))
    y = (X[:, ::2].sum(axis=1) < 0.0).astype(int)
    return train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)


def sum_up_tree_values(tree, field):
    """Perform depth first search across the tree and sum up values of requested fields

    Args:
        tree: Tree
            Tree to traverse
        field: str
            The name of the class field which values should be summed up
    Returns:
        float:
            The sum of all values found across the tree. None is replaces with 0.0
    """
    value = getattr(tree, field)
    if value is None:
        value = 0.0
    if tree.left_child is not None:
        value += sum_up_tree_values(tree.left_child, field)
    if tree.right_child is not None:
        value += sum_up_tree_values(tree.right_child, field)
    return value


def sum_up_forest_values(forest, field):
    """Sums up values of requested field in all the trees of a firest

    Args:
        forest: RandomForestClassifier
            Random Forest to go through
        field: str
            The name of the class field which values should be summed up
    Returns:
        float:
            The sum of all values found across all the trees of the forest.
    """
    value = 0
    for tree in forest.trees:
        value += sum_up_tree_values(tree, field)
    return value


def test_gini_index(func):
    def test(x, value):
        assert np.isclose(func(x), value), f'Should be {value} for {x}'
    test(np.array([]), 0.0)
    test(np.array([1]), 0.0)
    test(np.array([1, 0]), 0.5)
    test(np.array([1, 1, 0]), 4/9)
    trgt = np.random.default_rng(RANDOM_STATE).choice([0, 1], 20)
    test(trgt, 0.455)
    print('\033[92m All good!')


def test_gini_gain(func):
    def test(x, xs, value):
        assert np.isclose(func(x, xs), value), f'Should be {value} for {x} and {xs}'
    test(np.array([1, 1, 0]), [np.array([1, 1]), np.array([2])], 4/9)
    test(np.array([1, 1, 0]), [np.array([1]), np.array([1, 2])], 1/9)
    trgt = np.random.default_rng(RANDOM_STATE).choice([0, 1], 20)
    test(trgt, [trgt[:10], trgt[10:]], 0.045)
    print('\033[92m All good!')


def test_entropy(func):
    assert func(np.array([0])) == 0.0, 'Should be 0.0 if all elements are equal'
    assert func(np.array([1])) == 0.0, 'Should be 0.0 if all elements are equal'

    def test(x, value):
        assert np.isclose(func(x), value), f'Should be {value} for {x}'
    test(np.array([]), 0.0)
    test(np.array([1, 0]), 0.69314718)
    test(np.array([1, 1, 0]), 0.63651416)
    trgt = np.random.default_rng(RANDOM_STATE).choice([0, 1], 20)
    test(trgt, 0.64744663)
    print('\033[92m All good!')


def test_information_gain(func):
    def test(x, xs, value):
        assert np.isclose(func(x, xs), value), f'Should be {value} for {x} and {xs}'
    test(np.array([1, 1, 0]), [np.array([1, 1]), np.array([2])], 0.63651416)
    test(np.array([1, 1, 0]), [np.array([1]), np.array([1, 2])], 0.17441604)
    trgt = np.random.default_rng(RANDOM_STATE).choice([0, 1], 20)
    test(trgt, [trgt[:10], trgt[10:]], 0.05067183)
    print('\033[92m All good!')


def test_split_dataset(func):
    df = np.random.default_rng(RANDOM_STATE).normal(size=(5, 2))
    trgt = np.random.default_rng(RANDOM_STATE).integers(2, size=5)
    l_X, r_X, l_y, r_y = func(df, trgt, 0, 0)
    assert l_X is not None and l_y is not None, "Should not return None values"
    assert np.allclose(l_X, [[-0.27279702,  0.06677798], [-1.76050488,  1.08797011]])
    assert np.array_equal(l_y, [1, 1])
    l_X, r_X, l_y, r_y = func(df, trgt, 1, 0.1)
    assert l_X is not None and l_y is not None, "Should not return None values"
    assert np.allclose(l_X, [[1.33254869, -1.41820464], [-0.27279702,  0.06677798]])
    assert np.array_equal(l_y, [0, 1])
    print('\033[92m All good!')


def test_tree(Tree):
    rng = np.random.default_rng(RANDOM_STATE)
    df = rng.normal(size=(5, 3))
    y = rng.integers(2, size=5)
    df_test = rng.normal(size=(5, 3))

    tree = Tree(criterion='entropy', random_gen=np.random.default_rng(RANDOM_STATE))
    assert np.allclose(np.sort(tree._find_splits(df[:, 0])),
                       [-0.58359374, 0.31790047, 0.73637695, 1.17408836]), \
        "Your _find_splits function doesn't work right"
    assert np.allclose(tree._find_best_split(df, y, df.shape[1]),
                       [0, 0.73637695, 0.29110316]), \
        "Your _find_best_splits function doesn't work right"
    tree.fit(df, y, max_depth=0)
    assert tree.left_child is None and tree.right_child is None, \
        "Your tree grows more then allowed by max_depth."
    tree.fit(df, np.array([1, 1, 1, 1, 1]))
    assert tree.left_child is None and tree.right_child is None, \
        "Your tree grows even when it is pure"

    tree = Tree(criterion='entropy', random_gen=np.random.default_rng(RANDOM_STATE))
    tree.fit(df, y, max_depth=1)
    assert np.isclose(tree.threshold, 0.73637695) and tree.column_index == 0, \
        "The split values are not stored in the right way."
    assert tree.left_child is not None and tree.right_child is not None, \
        "Your tree doesn't grow children when it should."
    assert np.array_equal([tree.predict_row(np.array([x, 0, 0])) for x in [0.73, 0.74]],
                [0., 1.]), "Your predict_row method may be erroneous"

    tree = Tree(criterion='entropy', random_gen=np.random.default_rng(RANDOM_STATE))
    tree.fit(df, y)
    np.allclose([sum_up_tree_values(tree, field) for field in
                 ['threshold', 'outcome_probs', 'column_index']],
                [-0.11048649, 2.0, 2.0]), "Your fit method seem to have an error"
    assert np.allclose(tree.predict(df_test), [0., 0., 1., 0., 0.]),\
        "Your predict method may be erroneous"

    X_train, X_test, y_train, y_test = create_datasets()
    tree = Tree(criterion='gini', random_gen=np.random.default_rng(RANDOM_STATE))
    tree.fit(X_train, y_train, max_depth=3, feature_frac=0.7)

    assert np.allclose([sum_up_tree_values(tree, field) for field in
                                    ['threshold', 'outcome_probs', 'column_index']],
                       [0.28624208, 4.0, 28.0]), "Your fit method seems to have an error"

    y_pred = tree.predict(X_test)
    assert np.isclose(accuracy_score(y_test, y_pred), 0.78125), \
        "Your tree is not accurate enough enough"

    print('\033[92m All good!')


def test_random_forest(clf):
    X_train, X_test, y_train, y_test = create_datasets()
    rng = np.random.default_rng(RANDOM_STATE)
    model = clf(n_estimators=10, max_depth=4, feature_frac=None,
                                   criterion="entropy", random_gen=rng)
    model.fit(X_train, y_train)

    assert np.allclose([sum_up_forest_values(model, field) for field in
                                    ['threshold', 'outcome_probs', 'column_index']],
                       [-9.41975128, 45.0, 346.0]), "Your fit method seems to have an error"

    y_pred = model.predict(X_test)
    assert np.isclose(accuracy_score(y_test, y_pred), 0.71875), \
        "Your classifier is not accurate enough"
    print('\033[92m All good!')
