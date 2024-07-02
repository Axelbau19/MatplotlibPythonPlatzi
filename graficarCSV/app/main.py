import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('app/LEC_SpringPlayoffs_2024.csv')
    player = input("Name's player =>")
    result = utils.getDictPlayer(data,player)
    if len(result)>0:
        namesPlayer = result[0]
        labels,values = utils.getInfoPlayersGameGraph(namesPlayer)
        charts.generateBarCharts(labels,values)
        print(result[0])



if __name__ == '__main__':
    run()