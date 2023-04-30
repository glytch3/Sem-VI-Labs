import math
import numpy as np
import itertools
from collections import Counter
from itertools import combinations


def generateCandidateItemsets(k, level_frequent_itemsets):
    n_frequent_itemsets = len(level_frequent_itemsets)
    candidate_frequent_itemsets = []
    for i in range(n_frequent_itemsets):
        j = i + 1
        while (j < n_frequent_itemsets) and (level_frequent_itemsets[i][:k-1] == level_frequent_itemsets[j][:k-1]):
            candidate_itemset = level_frequent_itemsets[i][:k-1] + [level_frequent_itemsets[i][k-1]] + [level_frequent_itemsets[j][k-1]]
            candidate_itemset_pass = False
            if k == 1:
                candidate_itemset_pass = True
            elif (k == 2) and (candidate_itemset[-2:] in level_frequent_itemsets):
                candidate_itemset_pass = True
            elif all((list(_)+candidate_itemset[-2:]) in level_frequent_itemsets for _ in combinations(candidate_itemset[:-2], k-2)):
                candidate_itemset_pass = True
            if candidate_itemset_pass:
                candidate_frequent_itemsets.append(candidate_itemset)
            j += 1
    return candidate_frequent_itemsets

def generateMFCS(MFCS, infrequent_itemsets):
    MFCS = MFCS.copy()
    for infrequent_itemset in infrequent_itemsets:
        for MFCS_itemset in MFCS.copy():
            if all(_item in MFCS_itemset for _item in infrequent_itemset):
                MFCS.remove(MFCS_itemset)
                for item in infrequent_itemset:
                    updated_MFCS_itemset = MFCS_itemset.copy()
                    updated_MFCS_itemset.remove(item)
                    if not any(all(_item in _MFCS_itemset for _item in updated_MFCS_itemset) for _MFCS_itemset in MFCS):
                        MFCS.append(updated_MFCS_itemset)
    return MFCS

def MFSprune(candidate_itemsets, MFS):
    candidate_itemsets = candidate_itemsets.copy()
    for itemset in candidate_itemsets.copy():
        if any(all(_item in _MFS_itemset for _item in itemset) for _MFS_itemset in MFS):
            candidate_itemsets.remove(itemset)
    return candidate_itemsets

def MFCSprune(candidate_itemsets, MFCS):
    candidate_itemsets = candidate_itemsets.copy()
    for itemset in candidate_itemsets.copy():
        if not any(all(_item in _MFCS_itemset for _item in itemset) for _MFCS_itemset in MFCS):
            candidate_itemsets.remove(itemset)
    return candidate_itemsets

def pincerSearch(transactions, min_support):
    items = set()
    for transaction in transactions:
        items.update(transaction)
    items = sorted(list(items))
    k = 1
    level_frequent_itemsets = []
    candidate_frequent_itemsets = [[item] for item in items]
    level_infrequent_itemsets = []
    MFCS = [items.copy()]
    MFS = []
    print("MFCS = {}".format(MFCS))
    print("MFS = {}\n".format(MFS))
    ans=[]
    while candidate_frequent_itemsets:
        print("LEVEL {}: ".format(k))
        print("C{} = {}".format(k, candidate_frequent_itemsets))
        candidate_freq_itemsets_cnts = [0]*len(candidate_frequent_itemsets)
        MFCS_itemsets_cnts = [0]*len(MFCS)
        for transaction in transactions:
            for i, itemset in enumerate(candidate_frequent_itemsets):
                if all(_item in transaction for _item in itemset):
                    candidate_freq_itemsets_cnts[i] += 1
            for i, itemset in enumerate(MFCS):
                if all(_item in transaction for _item in itemset):
                    MFCS_itemsets_cnts[i] += 1

        for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts):
            print("{} -> {}".format(itemset, support), end=', ')
        print()

        for itemset, support in zip(MFCS, MFCS_itemsets_cnts):
            print("{} -> {}".format(itemset, support), end=', ')
        print()

        MFS.extend([itemset for itemset, support in zip(MFCS, MFCS_itemsets_cnts) if ((support >= min_support) and (itemset not in MFS))])
        print("MFS = {}".format(MFS))

        level_frequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts) if support >= min_support]
        level_infrequent_itemsets = [itemset for itemset, support in zip(candidate_frequent_itemsets, candidate_freq_itemsets_cnts) if support < min_support]

        print("L{} = {}".format(k, level_frequent_itemsets))
        print("S{} = {}".format(k, level_infrequent_itemsets))
        ans+=level_frequent_itemsets
        MFCS = generateMFCS(MFCS, level_infrequent_itemsets)
        print("MFCS = {}".format(MFCS))

        level_frequent_itemsets = MFSprune(level_frequent_itemsets, MFS)
        print("After Pruning: L{} = {}\n".format(k, level_frequent_itemsets))
        candidate_frequent_itemsets = generateCandidateItemsets(k, level_frequent_itemsets)
        candidate_frequent_itemsets = MFCSprune(candidate_frequent_itemsets, MFCS)
        k += 1

    return MFS,ans


def get_transactions():
    transactions = []
    while True:
        t = input("Enter transaction ")
        if t == '':
            break
        items = set(map(int, t.split(',')))
        transactions.append(items)
    return transactions

if __name__ == '__main__':
    transactions = get_transactions()
    min_support_count = int(input("Enter minimum support: "))
    MFS,ans = pincerSearch(transactions, min_support_count)
    print("MFS = {}".format(MFS))
    ans+=MFS
    result = []
    for item in ans:
        if item not in result:
            result.append(item)
    print("Frequent item set: ",result)


