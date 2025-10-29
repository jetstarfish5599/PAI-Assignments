# KarachiDeals System
#Create dic of list via sets
def processTransactions(transactionsList):
    custData = {}
    for t in transactionsList:
        cid, pid = t['customerId'], t['productId']
        if cid not in custData:
            custData[cid] = set()
        custData[cid].add(pid)
    return custData


# pair is bought together
def findFrequentPairs(customerData):
    pairCount = {}
    for cust, prods in customerData.items():
        plist = list(prods)
        for i in range(len(plist)):
            for j in range(i + 1, len(plist)):
                p1, p2 = sorted((plist[i], plist[j]))
                key = (p1, p2)
                pairCount[key] = pairCount.get(key, 0) + 1
    return pairCount


# top product pairs
def getRecommendations(targetProductId, frequentPairs):
    recs = {}
    for (p1, p2), c in frequentPairs.items():
        if targetProductId in (p1, p2):
            other = p2 if p1 == targetProductId else p1
            recs[other] = recs.get(other, 0) + c
    ranked = sorted(recs.items(), key=lambda x: x[1], reverse=True)
    return ranked


# prints report
def generateReport(targetProductId, recommendations, catalog):
    print(f"\nProducts often bought with: {catalog.get(targetProductId, targetProductId)}")
    print("-" * 40)
    if not recommendations:
        print("No related items found.")
        return
    ids, counts = zip(*recommendations)
    for i, (pid, cnt) in enumerate(zip(ids, counts), start=1):
        print(f"{i}. {catalog.get(pid, pid)} --> {cnt} times")


# sample use
transactionLog = [
    {'orderId': 10001, 'customerId': 'cust_ahmed', 'productId': 'prod_1'},
    {'orderId': 10001, 'customerId': 'cust_ahmed', 'productId': 'prod_2'},
    {'orderId': 10002, 'customerId': 'cust_bisma', 'productId': 'prod_1'},
    {'orderId': 10002, 'customerId': 'cust_bisma', 'productId': 'prod_3'},
    {'orderId': 10003, 'customerId': 'cust_ahmed', 'productId': 'prod_2'},
    {'orderId': 10004, 'customerId': 'cust_fasal', 'productId': 'prod_2'},
    {'orderId': 10004, 'customerId': 'cust_Fasal', 'productId': 'prod_3'},
]

productCatalog = {
    'prod_1': 'Mouse',
    'prod_2': 'Keyboard',
    'prod_3': 'USB'
}

#main
custData = processTransactions(transactionLog)
pairs = findFrequentPairs(custData)
target = 'prod_1'
recs = getRecommendations(target, pairs)
generateReport(target, recs, productCatalog)


custData = processTransactions(transactionLog)
pairs = findFrequentPairs(custData)
target1 = 'prod_2'
recs1 = getRecommendations(target1, pairs)
generateReport(target1, recs1, productCatalog)
target2 = 'prod_3'
recs2 = getRecommendations(target2, pairs)
generateReport(target2, recs2, productCatalog)