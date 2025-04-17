#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598
'''
usage:
    python3 csv_tools.py --input=/home/slam/YuFeng/BasicPython/Chapter10/datas.csv
'''

import csv
import argparse
import openpyxl

from abc import abstractmethod
from pathlib import Path
from typing import override


class FileAdaptee:
    def __init__(self, file: Path) -> None:
        self.file_path_: Path = file
        self.file_ = None
        self.data_ = None

    @staticmethod
    def CheckFileExistence(file_path: Path) -> bool:
        return file_path.exists()

    @abstractmethod
    def LoadFile(self) -> bool:
        pass

    @abstractmethod
    def GetDatasbyKeyword(self, keyword: str):
        pass


class CSVFileAdaptee(FileAdaptee):
    def __init__(self, file: Path) -> None:
        super().__init__(file)
        self.csv_reader_ = None

    @override
    def LoadFile(self) -> bool:
        if not CSVFileAdaptee.CheckFileExistence(self.file_path_):
            return False
        self.file_ = open(file=self.file_path_.as_posix(),
                          mode="r", encoding="UTF-8-sig")
        self.csv_reader_ = csv.DictReader(self.file_)
        return True

    @override
    def GetDatasbyKeyword(self, keyword: str):
        self.data_ = {}
        for line in self.csv_reader_:
            year = line.get(keyword)
            if year not in self.data_:
                self.data_[year] = [line]
            else:
                self.data_[year].append(line)
        return self.data_

    def __del__(self):
        self.file_.close()


class ExcelWriter:
    def __init__(self):
        self.loader_ = None
        pass

    def SetLoader(self, loader: FileAdaptee):
        self.loader_ = loader

    def DumpExcel(self, keyword: str, output: Path) -> bool:
        if not self.loader_.LoadFile():
            return False

        keyword_datas = self.loader_.GetDatasbyKeyword(keyword)

        dest_wb = openpyxl.Workbook()
        sheet_map = {}

        for k, v in keyword_datas.items():
            sheet = dest_wb.create_sheet(k)
            all_titles = []
            for title_data in v:
                each_titles = list(title_data.keys())
                for t in each_titles:
                    if t not in all_titles:
                        all_titles.append(t)

            sheet.append(all_titles)
            sheet_map[k] = sheet

        for k, v in keyword_datas.items():
            sheet = sheet_map.get(k)
            for title_data in v:
                l = list(title_data.values())
                sheet.append(l)

        dest_wb.save(output.as_posix())
        return True


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    _ = args.add_argument("--input", type=str, default="", required=True)
    _ = args.add_argument("--keyword", type=str, default="年份", required=False)
    args = args.parse_args()

    input: Path = Path(args.input)
    keyword = str(args.keyword)
    output: Path = input.parent/"result.xlsx"
    loader = CSVFileAdaptee(input)
    writer = ExcelWriter()
    writer.SetLoader(loader)
    _ = writer.DumpExcel(keyword, output)
    pass
