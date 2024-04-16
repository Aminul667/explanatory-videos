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
            col_labels=[Text("Size"), Text("Price"), Text(
                "Predicted Price"), Text("Actual-Predicted")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW}
        )

        # print("TablePrint", table[0])

        col_labs = table.get_col_labels()
        col_labs_predict = tablePredict.get_col_labels()

        col_labs.set_color(RED)
        table.scale(0.4).to_edge(UL)

        col_labs_predict.set_color(RED)
        tablePredict.scale(0.4).to_edge(UL)

        self.play(Write(table), run_time=3)
        self.wait()

        # self.remove(table)
        self.play(Write(tablePredict), run_time=3)
        self.remove(table)
        self.wait()

        ax = Axes(
            x_range=[0, 2000, 200],
            y_range=[0, 40000, 4000],
            x_length=10,
            # y_length=10,
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        )
        ax.scale(0.6).move_to(DOWN)

        dot_1 = Dot(ax.c2p(1000, 16000), color=GREEN)
        dot_2 = Dot(ax.c2p(1500, 33000), color=GREEN)
        dot_3 = Dot(ax.c2p(1800, 40000), color=GREEN)

        # graph = ax.plot(lambda x: 20*x, x_range=[0.001, 2000], use_smoothing=False)

        self.play(Write(ax), run_time=3)
        self.wait()

        self.play(Write(dot_1), Write(dot_2), Write(dot_3), run_time=3)
        self.wait()

        # self.play(Write(group), run_time=3)
        # self.wait()
        # self.add(ax, dot_1, dot_2, dot_3)

