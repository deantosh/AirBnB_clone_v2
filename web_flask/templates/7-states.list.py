<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>
            {% for state in states %}
                <LI>{{ state.id }}: <B>{{ state.name }}</B></LI>
            {% endfor %}
        </UL>
    </BODY>
</HTML>
