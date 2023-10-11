import calendar
import csv
import os


class CircadianRhythm:

    def __init__(self, date):
        self.year = date[:4]
        self.month = date[4:6]
        self.day = date[6:]
        self.first_meal_time = None
        self.last_meal_time = None
        self.sleep_duration = None
        self.wellness_changes = None

    def _menu(self):
        self.first_meal_time = input("첫 음식 섭취 시간: ")
        self.last_meal_time = input("마지막 음식 섭취 시간: ")
        self.sleep_duration = input("수면 시간: ")
        self.wellness_changes = input("건강, 기운, 기분상에 주목할 만한 변화: ")

    def insert(self):
        self._menu()
        self._save()

    def delete(self):
        self.first_meal_time = None
        self.last_meal_time = None
        self.sleep_duration = None
        self.wellness_changes = None
        self._save()

    def _save(self):

        dir_path = f'data/{self.year}'
        file_path = f'{dir_path}/{self.month}.csv'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        if os.path.exists(file_path):
            with open(file_path, "r", encoding='utf-8') as file:
                data = list(csv.reader(file))

            for line in data[1:]:
                if line[0] == self.day:
                    line[1] = self.first_meal_time
                    line[2] = self.last_meal_time
                    line[3] = self.sleep_duration
                    line[4] = self.wellness_changes
                    break

            with open(file_path, 'w', newline='', encoding='utf-8') as file:
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
                    initial_data.append([self.day, self.first_meal_time, self.last_meal_time, self.sleep_duration,
                                         self.wellness_changes])
                else:
                    initial_data.append([day, None, None, None, None])

            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(initial_data)