from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from samklang_project import Project

class Sprint(models.Model):
    """Sprint or milestone"""

    name = models.CharField(_('name'), max_length=60)
    description = models.TextField(_('description'), blank=True)
    start = models.DateField(_('start'), blank=True, null=True)
    end = models.DateField(_('end'), blank=True, null=True)

    class Meta:
        verbose_name = _('sprint')
        verbose_name_plural = _('sprints')

    def __unicode__(self):
        return self.name

    #@models.permalink
    #def get_absolute_url(self):
        #return ('view_or_url_name' )


class Issue(models.Model):
    """User stories or issues"""

    summary = models.TextField()
    sprint = models.ForeignKey(Sprint, verbose_name=_('sprint'), null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_('project'), null=True, blank=True)
    ongoing = models.BooleanField(_('ongoing'), default=False)
    finished = models.BooleanField(_('finished'), default=False)
    reviewed = models.BooleanField(_('reviewed'), default=False)
    estimated = models.SmallIntegerField(_('estimated'), null=True, blank=True)
    priority = models.SmallIntegerField(_('priority'), null=True, blank=True)

    reporter = models.ForeignKey(User, verbose_name=_('reporter'), null=True, blank=True)
    assignee = models.ForeignKey(User, verbose_name=_('assignee'), null=True, blank=True)
    reviewer = models.ForeignKey(User, verbose_name=_('reviewer'), null=True, blank=True)

    follows = models.ForeignKey('self', related_name='preceds', verbose_name=_('follows'), blank=True)

    # later:
    # resolution
    # status

    class Meta:
        verbose_name = _('issue')
        verbose_name_plural = _('issues')

    def __unicode__(self):
        return "%d: %s" % (self.pk, self.summary[:100])

    #@models.permalink
    #def get_absolute_url(self):
        #return ('view_or_url_name' )


class Task(models.Model):
    """User level sub-tasks"""

    summary = models.TextField()

    reporter = models.ForeignKey(User, verbose_name=_('reporter'), null=True, blank=True)
    assignee = models.ForeignKey(User, verbose_name=_('assignee'), null=True, blank=True)

    created = models.DateTimeField(_('created'))
    finished = models.DateTimeField(_('finished'), null=True, blank=True)

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __unicode__(self):
        return "%d: %s" % (self.pk, self.summary[:50])

    #@models.permalink
    #def get_absolute_url(self):
        #return ('view_or_url_name' )


