import calendar
import csv
import os


class CircadianRhythm:

    def __init__(self, date):
        self.year = date[:4]
        self.month = date[4:6]
        self.day = date[6:]
        self.first_meal_time = ''
        self.last_meal_time = ''
        self.sleep_duration = ''
        self.wellness_changes = ''

        self.dir_path = f'data/{self.year}'
        self.file_path = f'{self.dir_path}/{self.month}.csv'

    def _menu(self):
        data = self._data_reader()
        if data:
            for line in data[1:]:
                if line[0] == self.day:
                    self.first_meal_time = line[1]
                    self.last_meal_time = line[2]
                    self.sleep_duration = line[3]
                    self.wellness_changes = line[4]
                    break

        if not self.first_meal_time:
            self.first_meal_time = input("첫 음식 섭취 시간: ")
        if not self.last_meal_time:
            self.last_meal_time = input("마지막 음식 섭취 시간: ")
        if not self.sleep_duration:
            self.sleep_duration = input("수면 시간: ")
        if not self.wellness_changes:
            self.wellness_changes = input("건강, 기운, 기분상에 주목할 만한 변화: ")

        print(f"first meal time: {self.first_meal_time}")
        print(f"last meal time: {self.last_meal_time}")
        print(f"sleep_duration: {self.sleep_duration}")
        print(f"wellness_changes: {self.wellness_changes}")

    def _data_reader(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding='utf-8') as file:
                return list(csv.reader(file))
        else:
            return False

    def insert(self):
        self._menu()
        self._save()

    def delete(self):
        self.first_meal_time = ''
        self.last_meal_time = ''
        self.sleep_duration = ''
        self.wellness_changes = ''
        self._save()

    def _save(self):

        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)

        data = self._data_reader()
        if data:
            for line in data[1:]:
                if line[0] == self.day:
                    line[1] = self.first_meal_time
                    line[2] = self.last_meal_time
                    line[3] = self.sleep_duration
                    line[4] = self.wellness_changes
                    break

            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        else:
            header_list = ['날짜', '첫 음식 섭취 시간', '마지막 음식 섭취 시간', '수면 시간', '건강, 기운, 기분 상에 주목할 만한 변화']
            initial_data = [header_list]
            # 월의 마지막 날짜 구하기
            last_day = calendar.monthrange(int(self.year), int(self.month))[1]

            for day in range(1, last_day + 1):
                day = f'{day:02}'
                if day == self.day:
                    initial_data.append([self.day, self.first_meal_time, self.last_meal_time,
                                         self.sleep_duration, self.wellness_changes])
                else:
                    initial_data.append([day, '', '', '', ''])

            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(initial_data)