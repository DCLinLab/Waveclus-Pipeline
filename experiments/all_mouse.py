from sorter import WaveclusInterface
from pathlib import Path
from traceback import print_exc
import shutil


if __name__ == '__main__':
    raw_dir = Path(r'D:\Yongzhi_Sun\01_Raw_Data\Yongzhi_Sun\intan\curved_120\20240912_m1')
    res_dir = Path(r'G:\wavclus_result\curved_120\20240912_m1')
    sessions = sorted(raw_dir.rglob('imp*.csv'))
    for s in sessions:
        new_folder = res_dir / s.parent.relative_to(raw_dir)
        out =  new_folder / 'spikes.pkl.tgz'
        if out.exists():
            print(f'Skip {s.parent}')
            continue
        print(f'Do {s.parent}')
        try:
            new_folder.mkdir(exist_ok=True, parents=True)
            WaveclusInterface().sort(s.parent, out, s, time_range=(3, 13))
        except:
            shutil.rmtree(new_folder, ignore_errors=True)
            print_exc()
