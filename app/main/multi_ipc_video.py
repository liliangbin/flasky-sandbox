from flask import render_template

from app.utils.site import Site
from config import Config
from . import main
# TODO 2020/5/21 22:46 liliangbin  一键全部录制，全部停止

@main.route("/multi_ipc_video/", methods=["GET", "POST"])
def multi_ipc_video():
    ips = []

    path_in = './app/static/video/'
    path_out = '../static/video/'
    image_path = Config.UPLOAD_IMAGE_PATH
    document_path = Config.SAVE_DOCUMENT_PATH
    with open(document_path + "ipcConfig.txt", "r+") as  f:
        a = f.readlines()
    for i in a:
        ips.append(i)
    try:
        with open(document_path + "site_0.txt", "r+") as  f:
            a = f.readlines()
            print(a)
            frame_location = Site(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
    except Exception as e:
        frame_location = Site(0, 0, 0, 0)

    tmp2 = frame_location.locate_y + frame_location.move_y
    tmp1 = frame_location.locate_x + frame_location.move_x
    site_left_top = str(frame_location.locate_x) + ',' + str(frame_location.locate_y)
    site_left_bottom = str(frame_location.locate_x) + ',' + str(tmp2)

    site_right_top = str(tmp1) + ',' + str(frame_location.locate_y)
    site_right_bottom = str(tmp1) + ',' + str(tmp2)

    return render_template('multi_ipc_video.html',
                           ips=ips,
                           site_left_top=site_left_top,
                           site_left_bottom=site_left_bottom,
                           site_right_top=site_right_top,
                           site_right_bottom=site_right_bottom,
                           )
