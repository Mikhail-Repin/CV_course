import cv2 as cv
import numpy as np


def is_inside(bbox, point):
    if point[0] < bbox[0] or point[0] > bbox[0] + bbox[2] or point[1] < bbox[1] or point[1] > bbox[1] + bbox[3]:
        return False
    else:
        return True


class TicTacGame:
    def __init__(self, cross, circle, bg_img = 255*np.ones((700, 700, 3))):
        self.img = bg_img
        self.cross = cross
        self.circle = circle
        self.last_sign = [[0, (0, 0)]]
        self.history = np.zeros((3, 3))
        self.table_bbox = [0, 0, 0, 0]
        self.buttons = {}
        self.start = True
        self.has_win = False
        self.quit = False

    def check_win(self):
        for i in range(3):
            if self.history[i, :].sum() % 3 == 0 and self.history[i, 0]*self.history[i, 1]*self.history[i, 2] != 0:
                return True, i
        for i in range(3):
            if self.history[:, i].sum() % 3 == 0 and self.history[0, i]*self.history[1, i]*self.history[2, i] != 0:
                return True, i + 3
        if (self.history[0, 0] + self.history[1, 1] + self.history[2, 2]) % 3 == 0 and self.history[0, 0]*self.history[1, 1]*self.history[2, 2] != 0:
            return True, 6
        elif (self.history[2, 0] + self.history[1, 1] + self.history[0, 2]) % 3 == 0 and self.history[2, 0]*self.history[1, 1]*self.history[0, 2] != 0:
            return True, 7
        mult = 1
        for str in self.history:
            for val in str:
                mult *= val
        if mult != 0:
            return True, -1
        else:
            return False, -2

    def make_table(self):
        size = int(self.img.shape[0]*0.8)
        sc_x = (size//3)/self.circle.shape[1]
        sc_y = (size//3)/self.circle.shape[0]
        self.circle = cv.resize(self.circle, (size//3, size//3), self.circle, sc_x, sc_y)
        sc_x = (size//3)/self.cross.shape[1]
        sc_y = (size//3)/self.cross.shape[0]
        self.cross = cv.resize(self.cross, (size//3, size//3), self.cross, sc_x, sc_y)
        game_table = np.zeros((size, size, 3))
        for i in range(1, 3):
            coord = i*size//3
            cv.line(game_table, (coord, 0), (coord, size), (255, 255, 255), thickness=2)
            cv.line(game_table, (0, coord), (size, coord), (255, 255, 255), thickness=2)
        x_0 = (self.img.shape[1] - size)//2 - 1
        x_end = x_0 + size
        y_0 = (self.img.shape[0] - size)//2 - 1
        y_end = y_0 + size
        self.img[y_0:y_end, x_0:x_end, :] = game_table
        self.table_bbox = [x_0, y_0, size, size]

    def make_buttons(self):
        names = ["new", "back", "quit"]
        x_0 = int(self.img.shape[0] * 0.05)
        y_0 = 0
        step = 10
        size_x = int(self.img.shape[0] * 0.9 - 2 * step) // len(names)
        size_y = int(self.img.shape[1] * 0.05)
        for name in names:
            self.draw_button(name, x_0, y_0, size_x, size_y, clicked=False)
            self.buttons[name] = [x_0, y_0, size_x, size_y]

            x_0 = x_0 + size_x + step

    def draw_button(self, name, x_0=None, y_0=None, size_x=None, size_y=None, clicked=False):
        # Цвет кнопки в зависимости от состояния
        fill_color = (150, 150, 150) if clicked else (200, 200, 200)
        if x_0 is None or y_0 is None or size_x is None or size_y is None:
            x_0, y_0, size_x, size_y = self.buttons[name]
        cv.rectangle(self.img, (x_0, y_0), (x_0 + size_x, y_0 + size_y), fill_color, -1)
        cv.rectangle(self.img, (x_0, y_0), (x_0 + size_x, y_0 + size_y), (0, 0, 0), 3)
        font = cv.FONT_HERSHEY_SIMPLEX
        text_size = cv.getTextSize(name, font, 1, 2)[0]
        text_x = x_0 + (size_x - text_size[0]) // 2
        text_y = y_0 + (size_y + text_size[1]) // 2
        cv.putText(self.img, name, (text_x, text_y), font, 1, (0, 0, 0), 2, cv.LINE_AA)

    def finish_line(self, case):
        bias = int(self.table_bbox[2]*0.025)
        if case < 0:
            return
        elif case < 3:
             cv.line(self.img, (self.table_bbox[0] + bias, self.table_bbox[1] + int((case + 0.5)*self.table_bbox[2]//3)),\
                     (self.table_bbox[0] + self.table_bbox[2] - bias, self.table_bbox[1] + int((case + 0.5)*self.table_bbox[2]//3)), (255, 0, 0), 4)
        elif case < 6:
            cv.line(self.img, (self.table_bbox[0] + int((case-3 + 0.5)*self.table_bbox[2]//3), self.table_bbox[1] + bias),\
                    (self.table_bbox[0] + int((case-3 + 0.5)*self.table_bbox[2]//3), self.table_bbox[1] + self.table_bbox[2] - bias), (255, 0, 0), 4)
        elif case == 6:
            cv.line(self.img, (self.table_bbox[0] + bias, self.table_bbox[1] + bias),\
                    (self.table_bbox[0] + self.table_bbox[2] - bias, self.table_bbox[1] + self.table_bbox[2] - bias), (255, 0, 0), 4)
        else:
            cv.line(self.img, (self.table_bbox[0] + bias, self.table_bbox[1] + self.table_bbox[2] - bias),\
                    (self.table_bbox[0] + self.table_bbox[2] - bias, self.table_bbox[1] + bias), (255, 0, 0), 4)

    def update(self, sign, i, j):
        self.last_sign.append([sign, (i, j)])
        self.history[i, j] = sign
        win_check, case = self.check_win()
        if win_check:
            self.finish_line(case)
            self.has_win = True

    def draw_O(self, new_x, new_y):
        self.img[new_y:new_y+int(self.table_bbox[2]//3), new_x:new_x+int(self.table_bbox[2]//3), :] = self.circle
        # cv.circle(self.img, (new_x, new_y), int((self.table_bbox[2]//3)/2.2), (0, 255, 0))

    def draw_X(self, new_x, new_y):
        self.img[new_y:new_y+int(self.table_bbox[2]//3), new_x:new_x+int(self.table_bbox[2]//3), :] = self.cross
        # cv.line(self.img, (new_x, new_y), (new_x + int(self.table_bbox[2]//3), new_y + int(self.table_bbox[2]//3)), (0, 0, 255), 1)
        # cv.line(self.img, (new_x + int(self.table_bbox[2]//3), new_y), (new_x, new_y + int(self.table_bbox[2]//3)), (0, 0, 255), 1)

    def get_paste_coord(self, x, y):
        x -= self.table_bbox[0]
        y -= self.table_bbox[1]
        j = x//(self.table_bbox[2]//3)
        i = y//(self.table_bbox[3]//3)
        # if self.last_sign[-1][0] == -1 or self.last_sign[-1][0] == 0:
        #     new_x = self.table_bbox[2]//3 * j + self.table_bbox[2]//6 + self.table_bbox[0]
        #     new_y = self.table_bbox[3]//3 * i + self.table_bbox[3]//6 + self.table_bbox[1]
        # else:
        new_x = self.table_bbox[2]//3 * j + self.table_bbox[0]
        new_y = self.table_bbox[3]//3 * i + self.table_bbox[1]
        return new_x, new_y, i, j

    def go_back(self):
        self.history[self.last_sign[-1][1]] = 0
        self.last_sign.pop(-1)
        if self.has_win:
            self.has_win = False
        self.make_table()
        for i in range(self.history.shape[0]):
            for j in range(self.history.shape[0]):
                if self.history[i, j] == 1:
                    new_x = self.table_bbox[2]//3 * j + self.table_bbox[0]
                    new_y = self.table_bbox[3]//3 * i + self.table_bbox[1]
                    self.draw_O(new_x, new_y)
                    continue
                if self.history[i, j] == -1:
                    new_x = self.table_bbox[2]//3 * j + self.table_bbox[0]
                    new_y = self.table_bbox[3]//3 * i + self.table_bbox[1]
                    self.draw_X(new_x, new_y)


    @staticmethod
    def act(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            if is_inside(param.table_bbox, (x, y)) and not param.has_win:
                new_x, new_y, i, j = param.get_paste_coord(x, y)
                if param.history[i, j] != 0:
                    return
                if param.last_sign[-1][0] == -1 or param.last_sign[-1][0] == 0:
                    param.draw_O(new_x, new_y)
                    sign = 1
                else:
                    param.draw_X(new_x, new_y)
                    sign = -1
                param.update(sign, i, j)
                return
            elif is_inside(param.buttons["new"], (x, y)):
                param.draw_button("new", clicked=True)
                cv.imshow("TicTac", param.img)  # Обновляем окно с измененным изображением
                cv.waitKey(200)
                param.init_game()
                param.draw_button("new", clicked=False)
                cv.imshow("TicTac", param.img)
                return
            elif is_inside(param.buttons["back"], (x, y)) and (len(param.last_sign) - 1):
                param.draw_button("back", clicked=True)
                cv.imshow("TicTac", param.img)
                cv.waitKey(200)
                param.go_back()
                param.draw_button("back", clicked=False)
                cv.imshow("TicTac", param.img)
                return
            elif is_inside(param.buttons["quit"], (x, y)):
                param.draw_button("quit", clicked=True)
                cv.imshow("TicTac", param.img)
                cv.waitKey(200)
                param.quit = True
                param.draw_button("quit", clicked=False)
                cv.imshow("TicTac", param.img)
                return

    def init_game(self):
        self.last_sign = [[0, (0, 0)]]
        self.history = np.zeros((3, 3))
        self.buttons = {}
        self.make_table()
        self.make_buttons()
        self.start = False
        self.has_win = False
        self.quit = False

    def start_game(self):
        cv.startWindowThread()
        cv.namedWindow("TicTac")
        cv.setMouseCallback("TicTac", TicTacGame.act, self)
        while True:
            if self.quit:
                break
            if self.start:
                self.init_game()
            cv.imshow("TicTac", self.img)
            if cv.waitKey(1) & 0xFF == ord("q"):
                self.quit = True
            if self.has_win and cv.waitKey(1) & 0xFF == ord("\r"):
                self.start = True
        cv.destroyAllWindows()
        return


if __name__ == "__main__":
    print("============USAGE==============\n",\
          "press ENTER to start a new game\n",\
          "press q to quit the game\n",\
          "also you can use buttons\n",\
          "==============================")
    backgr_img = cv.imread('back_ground.jpg')
    backgr_img = cv.resize(backgr_img, (720, 720), backgr_img)
    cross = cv.imread('cross.jpg')
    circle = cv.imread('circle.jpg')
    game = TicTacGame(cross, circle, backgr_img)
    game.start_game()
