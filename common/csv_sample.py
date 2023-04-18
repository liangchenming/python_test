import csv
import fileinput


# from casemysql.case_mysql import SampleInfo


class CsvUtil:
    # 写入字段
    def write_sample_csv(self, data):
        with open('/Users/motong/PycharmProjects/pythontest/testcase/csv/' + 'out_sample.csv', mode='w',
                  encoding='utf-8', newline='') as file_obj:
            team_name = data[0]
            team_item = data[1]
            writer = csv.writer(file_obj)
            writer.writerow(team_name)
            writer.writerows(team_item)
            # for item in team_item:
            #     writer.writerow(item)
            file_obj.close()

    # # 循环写入子项
    # def write_sample_item(self, data):
    #     with open('/Users/motong/PycharmProjects/pythontest/testcase/csv/' + 'out_sample.csv', mode='a', encoding='utf-8') as file_obj:
    #         writer = csv.writer(file_obj)
    #         for item in data:
    #             writer.writerow(item)
