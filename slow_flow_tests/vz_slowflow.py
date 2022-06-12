import os
import os.path as osp
from os.path import splitext as spt
from glob import glob

from PIL import Image
import numpy as np

def read_gen(file_name):
    suf = spt(file_name)[-1]
    if suf == '.ppm':
        return Image.open(file_name)
    elif suf == '.flo':
        return read_flo_as_float32(file_name).astype(np.float32)
    return []

def read_flo_as_float32(filename):
    with open(filename, 'rb') as file:
        magic = np.fromfile(file, np.float32, count=1)
        assert(202021.25 == magic), "Magic number incorrect. Invalid .flo file"
        w = np.fromfile(file, np.int32, count=1)[0]
        h = np.fromfile(file, np.int32, count=1)[0]
        data = np.fromfile(file, np.float32, count=2*h*w)
    data2D = np.resize(data, (h, w, 2))
    return data2D

def make_color_wheel():
    RY, YG, GC, CB, BM, MR = 15, 6, 4, 11, 13, 6

    ncols = RY + YG + GC + CB + BM + MR
    colorwheel = np.zeros([ncols, 3])
    col = 0
    # RY
    colorwheel[0:RY, 0] = 255
    colorwheel[0:RY, 1] = np.transpose(np.floor(255*np.arange(0, RY) / RY))
    col += RY
    # YG
    colorwheel[col:col+YG, 0] = 255 - np.transpose(np.floor(255*np.arange(0, YG) / YG))
    colorwheel[col:col+YG, 1] = 255
    col += YG
    # GC
    colorwheel[col:col+GC, 1] = 255
    colorwheel[col:col+GC, 2] = np.transpose(np.floor(255*np.arange(0, GC) / GC))
    col += GC
    # CB
    colorwheel[col:col+CB, 1] = 255 - np.transpose(np.floor(255*np.arange(0, CB) / CB))
    colorwheel[col:col+CB, 2] = 255
    col += CB
    # BM
    colorwheel[col:col+BM, 2] = 255
    colorwheel[col:col+BM, 0] = np.transpose(np.floor(255*np.arange(0, BM) / BM))
    col += + BM
    # MR
    colorwheel[col:col+MR, 2] = 255 - np.transpose(np.floor(255 * np.arange(0, MR) / MR))
    colorwheel[col:col+MR, 0] = 255
    return colorwheel

def compute_color(u, v):
    [h, w] = u.shape
    img = np.zeros([h, w, 3])
    nanIdx = np.isnan(u) | np.isnan(v)
    u[nanIdx], v[nanIdx] = 0, 0

    colorwheel = make_color_wheel()
    ncols = np.size(colorwheel, 0)
    rad = np.sqrt(u**2+v**2)
    a = np.arctan2(-v, -u) / np.pi
    fk = (a+1) / 2 * (ncols - 1) + 1
    k0 = np.floor(fk).astype(int)
    k1 = k0 + 1
    k1[k1 == ncols+1] = 1
    f = fk - k0

    for i in range(0, np.size(colorwheel,1)):
        tmp = colorwheel[:, i]
        col0 = tmp[k0-1] / 255
        col1 = tmp[k1-1] / 255
        col = (1-f) * col0 + f * col1

        idx = rad <= 1
        col[idx] = 1-rad[idx]*(1-col[idx])
        notidx = np.logical_not(idx)

        col[notidx] *= 0.75
        img[:, :, i] = np.uint8(np.floor(255 * col*(1-nanIdx)))
    return img

def flow_to_image(flow):
    u, v = flow[:, :, 0], flow[:, :, 1]

    maxu, maxv, minu, minv = -100., -100., 100., 100.
    UNKNOWN_FLOW_THRESH, SMALLFLOW, LARGEFLOW = 1e7, 0.0, 1e8

    idxUnknow = (abs(u) > UNKNOWN_FLOW_THRESH) | (abs(v) > UNKNOWN_FLOW_THRESH)
    u[idxUnknow] , v[idxUnknow] = 0, 0

    maxu, minu = max(maxu, np.max(u)), min(minu, np.min(u))
    maxv, minv = max(maxv, np.max(v)), min(minv, np.min(v))

    rad = np.sqrt(u ** 2 + v ** 2)
    maxrad = max(-1, np.max(rad))

    u, v = u /(maxrad + np.finfo(float).eps), v /(maxrad + np.finfo(float).eps)

    img = compute_color(u, v)
    idx = np.repeat(idxUnknow[:, :, np.newaxis], 3, axis=2)
    img[idx] = 0
    return np.uint8(img)

if __name__ == '__main__':
    
    Image.fromarray(flow_to_image(read_gen("slow_flow_test/seq14_0000000.flo"))).save("slow_flow_test/seq14_0000000_gt.png")