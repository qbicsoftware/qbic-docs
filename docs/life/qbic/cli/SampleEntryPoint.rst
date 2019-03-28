.. java:import:: org.apache.logging.log4j LogManager

.. java:import:: org.apache.logging.log4j Logger

SampleEntryPoint
================

.. java:package:: life.qbic.cli
   :noindex:

.. java:type:: public class SampleEntryPoint

   Entry point for the Sample command-line Tool application. The purpose of this class is to act as a bridge between the command line and the \ *real*\  implementation of a tool by using a \ :java:ref:`ToolExecutor`\ .

Methods
-------
main
^^^^

.. java:method:: public static void main(String[] args)
   :outertype: SampleEntryPoint

   Main method.

   :param args: the command-line arguments.

