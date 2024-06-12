def find_runner_up_score(n, scores):
    unique_scores = set(scores)
    sorted_scores = sorted(unique_scores, reverse=True)
    return sorted_scores[1]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_runner_up_score(n, arr))
