from manim import *


class MachineLearning(Scene):
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
            col_labels=[Text("Size"), Text("Price"), Text(
                "Predicted Price"), Text("Actual-Predicted")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW}
        )

        col_labs = table.get_col_labels()
        col_labs_predict = tablePredict.get_col_labels()

        col_labs.set_color(RED)
        table.scale(0.4).to_edge(UL)

        col_labs_predict.set_color(RED)
        tablePredict.scale(0.4).to_edge(UL)

        self.play(Write(table), run_time=3)
        self.wait()

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

        dot_group = VGroup(dot_1, dot_2, dot_3)

        # graph = ax.plot(lambda x: 20*x, x_range=[0.001, 2000], use_smoothing=False)

        self.play(Write(ax), run_time=3)
        self.wait()

        self.play(Write(dot_group), run_time=3)
        self.wait()

        line_v = ax.get_vertical_line(dot_1.get_center(), color=RED)
        line_h = ax.get_horizontal_line(dot_1.get_center(), color=RED)

        line_group = VGroup()

        for i in [dot_1, dot_2, dot_3]:
            line_v = ax.get_vertical_line(i.get_center(), color=RED)
            line_h = ax.get_horizontal_line(i.get_center(), color=RED)

            line_group.add(line_v)
            line_group.add(line_h)

            self.play(Create(line_v), Create(line_h))
            self.wait()

        self.play(FadeOut(line_group))
        self.wait()

        equation = MathTex("y_{predict} = 20x_{size}").next_to(tablePredict, RIGHT, buff=1)
        self.play(Write(equation))

        graph = ax.plot(lambda x: 25*x, x_range=[0.001, 2000], use_smoothing=False)
        graph.set_color(BLUE)

        self.play(Create(graph))

