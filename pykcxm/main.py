import datasource
import ui


def main():
    ui.MainWindow('国内各省市新型冠状病毒肺炎疫情状况实时追踪', datasource.names())


if __name__ == '__main__':
    main()
