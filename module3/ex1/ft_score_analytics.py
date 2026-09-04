import sys


def score_analysis(scores: list) -> dict:
    stats = {}
    stats["number"] = len(scores)
    stats["total"] = sum(scores)
    stats["average"] = sum(scores) / len(scores)
    stats["max"] = max(scores)
    stats["min"] = min(scores)
    stats["range"] = max(scores) - min(scores)
    return stats


def get_score(score: str) -> int:
    try:
        num = int(score)
    except ValueError:
        print(f"Invalid parameter: '{score}'")
        return None
    return num


def main() -> None:
    print("=== Player Score Analytics :3 ===")
    score_list = [get_score(score) for score in sys.argv[1:]
                  if get_score(score) is not None]
    if len(score_list) == 0:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    stats = score_analysis(score_list)
    print(f"Scoreboard: {score_list}")
    print(f"Total players: {stats["number"]}")
    print(f"Total score: {stats["total"]}")
    print(f"Average score: {stats["average"]}")
    print(f"Highest score ;3 : {stats["max"]}")
    print(f"Lowest score :( : {stats["min"]}")
    print(f"Score range: {stats["range"]}\n")


if __name__ == "__main__":
    main()
