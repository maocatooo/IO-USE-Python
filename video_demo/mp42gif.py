from moviepy.editor import VideoFileClip
import imageio

'''
使用视频里面的片段做封面
'''


class VideoInfo(object):

    def __init__(self, filename, cut_count=3):
        """

        :param filename: 视频的路径
        :param cut_count: 截取多少个gif
        """
        self.clip = VideoFileClip(filename)
        self.cut_count = cut_count
        # 视频时长
        self.video_time = int(self.clip.duration)

    #
    # def video_time(self):
    #     # 获取视频时长
    #     return self.clip.duration
    def _step(self):
        # 计算步长
        return int(self.video_time / self.cut_count - 1)

    def _cut(self, s_time, e_time, resize_w=240, resize_h=160, fps=None):
        c1 = self.clip.subclip(s_time, e_time).resize((resize_w, resize_h))
        if fps is None:
            fps = self.clip.fps
        for frame in c1.iter_frames(fps=fps, dtype='uint8'):
            yield frame

    def _get(self):
        step = self._step()
        datas = []
        if step <= 1:
            for frame in self._cut(0, self.video_time):
                datas.append(frame)
        else:
            start = 0
            for i in range(self.cut_count):
                pass
        return datas

    def create_gif(self):
        c = self._get()
        imageio.mimsave('newfirst.gif', c, 'GIF', duration=1 / 24)
