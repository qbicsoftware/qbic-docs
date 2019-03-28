.. java:import:: org.apache.logging.log4j LogManager

.. java:import:: org.apache.logging.log4j Logger

SampleTool
==========

.. java:package:: life.qbic.cli
   :noindex:

.. java:type:: public class SampleTool extends QBiCTool<SampleCommand>

   Implementation of Sample command-line Tool. Its command-line arguments are contained in instances of \ :java:ref:`SampleCommand`\ .

Constructors
------------
SampleTool
^^^^^^^^^^

.. java:constructor:: public SampleTool(SampleCommand command)
   :outertype: SampleTool

   Constructor.

   :param command: an object that represents the parsed command-line arguments.

Methods
-------
execute
^^^^^^^

.. java:method:: @Override public void execute()
   :outertype: SampleTool

