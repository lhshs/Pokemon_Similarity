import sys
import click
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # tf CPU 관련 출력 삭제 
import warnings
warnings.filterwarnings('ignore')

from data import load
from model import similarity



## cli 에서 입력받을 곳 
@click.command()
@click.option('--first_name', 
              type = click.STRING, 
              prompt='First Pokemon Name',
              help='첫 번째 포켓몬 이름')
@click.option('--second_name', 
              type = click.STRING, 
              prompt='Second Pokemon Name',
              help='첫 번째 포켓몬과 유사도 측정할 두 번째 포켓몬 이름')


def start(first_name, second_name):
    if (first_name not in load.confirm()) or (second_name not in load.confirm()):
        print()
        print(' !!!- 포켓몬이 목록에 없습니다 -!!! ')
        print('      - 이름만 입력해주세요 -       ')
        print()
        sys.exit(1)      # 포켓몬 이름이 없다면 종료 
    else:
        print('<<<<< START >>>>>')
        print(f"  << Get Similar Between {first_name} & {second_name} >>  ")
        return similarity.similar_output(first_name, second_name)


if __name__ == '__main__':
    start()

