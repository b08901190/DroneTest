import distance2location as d2l 
import uwb_read as u
import Distance as d

anchor_positions = d.set_anchor_positions()
while True :
    dis = u.dis_to_anchors()
    # print("dis",dis)
    real_position = d.real_positions(dis,anchor_positions)
    print("real_positionn",real_position)
