from manim import *


class TableExamples(Scene):
    def construct(self):
        data = [
            ["1200", "25000"],
            ["1500", "30000"],
            ["1800", "35000"]
        ]
        dataPredict = [
            ["1200", "25000", "", ""],
            ["1500", "30000", "", ""],
            ["1800", "35000", "", ""]
        ]

        
        table = Table(
            data,
            # row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("Size"), Text("Price")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW}
        )
        tablePredict = Table(
            dataPredict,
            # row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("Size"), Text("Price"), Text("Predicted Price"), Text("Actual-Predicted")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW}
        )

        # print("TablePrint", table[0])

        col_labs = table.get_col_labels()
        col_labs_predict = tablePredict.get_col_labels()

        col_labs.set_color(RED)
        table.scale(0.4).to_edge(LEFT)

        col_labs_predict.set_color(RED)
        tablePredict.scale(0.4).to_edge(LEFT)

        self.play(Write(table), run_time=3)
        self.wait()

        # self.remove(table)
        self.play(Write(tablePredict), run_time=3)
        self.remove(table)
        self.wait()
