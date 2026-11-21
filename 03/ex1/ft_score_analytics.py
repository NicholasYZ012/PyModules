import sys

def processing(scores: list[int]) -> list[int]:
    try:
        proc = {
            'plycount': len(scores),
            'totscore': sum(scores),
            'avgscore': sum(scores) / len(scores),
            'max': max(scores),
            'min': min(scores),
            'range': max(scores) - min(scores)
        }
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except TypeError:
        pass


if __name__ == '__main__':
    n = len(sys.argv) - 1
    scores = sys.argv[1:]
    print(f'Submitted scores: {scores}')